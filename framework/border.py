from .component import Component
from typing import Tuple

class Border():
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
    def handle_component_collision(self, component: Component):
        hitbox = component.get_hitbox()
        vel = component.vel
        if hitbox.left() <= 0:
            component.vel.set_x(max(vel.x, -1 * vel.x))
        elif hitbox.right() >= self.width:
            component.vel.set_x(min(vel.x, -1 * vel.x))

        if hitbox.bottom() <= 0:
            component.vel.set_y(max(vel.y, -1 * vel.y))
        elif hitbox.top() >= self.height:
            component.vel.set_y(min(vel.y, -1 * vel.y))