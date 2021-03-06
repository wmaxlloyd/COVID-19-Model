import pyglet
from typing import Set, List, Tuple
from .component import Component
from .hitbox import Hitbox
from pyglet.gl import glClear, GL_COLOR_BUFFER_BIT
from .generator import ComponentGenerator
import uuid
from .border import Border
from .scene_section_manager import SceneSectionManager
from .reporter import Reporter

class Scene():
    def __init__(self, section_dimensions: Tuple[int, int] = (5,5)):
        self.__window = pyglet.window.Window()
        self.__width = self.__window.width
        self.__height = self.__window.height
        self.__components: Set[Component] = set()
        self.__border = Border(self.__width, self.__height)
        self.__section_manager = SceneSectionManager(self, 10, 10)
        self.__reporters: List[Reporter] = []
        self.__time_step = 0

        @self.__window.event
        def on_draw():
            self.draw()

    def generator(self, ComponentConstructor: Component):
        return ComponentGenerator(self, ComponentConstructor)
    
    def width(self):
        return self.__width
    
    def height(self):
        return self.__height
    
    def border(self):
        return self.__border

    def add_componenet(self, component: Component):
        self.__components.add(component)
        self.__section_manager.classify_component(component)
    
    def update_state(self, *args):
        self.__section_manager.handle_collisions()
        self.__section_manager.reset()
        for component in self.__components:
            component.update_state()
            self.__section_manager.classify_component(component)
        for reporter in self.__reporters:
            reporter.time_step_finished(self.__time_step)
        self.__time_step += 1

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        for componet in self.__components:
            componet.draw()

    def contains_collision_with(self, component: Component) -> bool:
        for scene_component in self.__components:
            if scene_component.is_collision(component):
                return True
        return False
    
    def add_reporter(self, reporter: Reporter):
        self.__reporters.append(reporter)
    
    def run(self):
        pyglet.clock.schedule(self.update_state, 1/10)
        pyglet.app.run()
