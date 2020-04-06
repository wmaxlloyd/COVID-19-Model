from pyglet.window import Window
from typing import Dict
from .component import Component
from .collison import Collision
from .hitbox import Hitbox
from pyglet.gl import glClear, GL_COLOR_BUFFER_BIT
from framework.random import Random
import uuid
from .border import Border

class Scene():
    def __init__(self, window: Window):
        self.width = window.width
        self.height = window.height
        self.window = window
        self.components: Dict[str, Component] = {}
        self.speed_limits = (2,5)
        self.border = Border(self.width, self.height)

    def generator(self):
        return Random(self)

    def add_componenet(self, component: Component):
        key = str(uuid.uuid4())
        self.components[key] = component
    
    def update_state(self, *args):
        for _, component in self.components.items():
            component.update_position()
        self.__handle_collisions()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        for _, componet in self.components.items():
            componet.draw()
    
    # def __find_collisions(self):
    #     self.bucket_componenets()
    #     pass

    def __handle_collisions(self):
        items = list(self.components.items())
        for i in range(len(items)):
            component = items[i][1]
            self.border.handle_component_collision(component)
            for j in range(i + 1, len(items)):
                component2 = items[j][1]
                Collision.handle(component, component2)

    def contains_collision_with(self, component: Component) -> bool:
        for (_, scene_component) in self.components.items():
            if scene_component.is_collision(component):
                return True
        return False
