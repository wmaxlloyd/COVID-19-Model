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
            component.vel.array[0] = max(vel.x(), -1 * vel.x())
        elif hitbox.right() >= self.width:
            component.vel.array[0] = min(vel.x(), -1 * vel.x())

        if hitbox.bottom() <= 0:
            component.vel.array[1] = max(vel.y(), -1 * vel.y())
        elif hitbox.top() >= self.height:
            component.vel.array[1] = min(vel.y(), -1 * vel.y())