from pyglet.window import Window
from typing import Set, List, Tuple
from .component import Component
from .hitbox import Hitbox
from pyglet.gl import glClear, GL_COLOR_BUFFER_BIT
from framework.random import Random
import uuid
from .border import Border
from .scene_section_manager import SceneSectionManager

class Scene():
    def __init__(self, window: Window, section_dimensions: Tuple[int, int] = (5,5)):
        self.__width = window.width
        self.__height = window.height
        self.__window = window
        self.__components: Set[Component] = set()
        self.__border = Border(self.__width, self.__height)
        self.__section_manager = SceneSectionManager(self, 10, 10)

    def generator(self, **kwargs):
        return Random(self, kwargs)
    
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
            component.update_position()
            self.__section_manager.classify_component(component)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.__section_manager.draw_sections()
        for componet in self.__components:
            componet.draw()

    def contains_collision_with(self, component: Component) -> bool:
        for scene_component in self.__components:
            if scene_component.is_collision(component):
                return True
        return False
