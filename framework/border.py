from .component import Component
from typing import Tuple
from .vector import VectorDirection

class Border():
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
    def handle_component_collision(self, component: Component):
        hitbox = component.get_hitbox()
        vel = component.vel
        if hitbox.left() <= 0:
            component.vel.set_x_direction(VectorDirection.POSITIVE)
        elif hitbox.right() >= self.width:
            component.vel.set_x_direction(VectorDirection.NEGATIVE)

        if hitbox.bottom() <= 0:
            component.vel.set_y_direction(VectorDirection.POSITIVE)
        elif hitbox.top() >= self.height:
            component.vel.set_y_direction(VectorDirection.NEGATIVE)