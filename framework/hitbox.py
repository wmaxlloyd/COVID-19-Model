from typing import Tuple, TYPE_CHECKING
from .vector import Vector

if TYPE_CHECKING:
    from .component import Component

class Hitbox:
    def __init__(self, component: 'Component', width: Tuple[float, float], height: Tuple[float, float]):
        self.component = component
        self.width_range = tuple(sorted(width))
        self.height_range = tuple(sorted(height))
    
    def get_coordinates(self) -> Tuple[Vector, Vector, Vector, Vector]:
        return (
            Vector(self.left(), self.top()), 
            Vector(self.right(), self.top()), 
            Vector(self.left(), self.bottom()),
            Vector(self.right(), self.bottom()),
        )
    
    def left(self):
        return self.component.pos.x() + self.width_range[0]
    
    def right(self):
        return self.component.pos.x() + self.width_range[1] 
    
    def top(self):
        return self.component.pos.y() + self.height_range[1]
    
    def bottom(self):
        return self.component.pos.y() + self.height_range[0]

    def contains_point(self, point: Vector):
        point_x, point_y = point.array
        if not self.left() <= point_x <= self.right():
            return False
        if not self.bottom() <= point_y <= self.top():
            return False
        return True

    def intersects(self, hitbox: 'Hitbox') -> bool:
        if (
            self.bottom() > hitbox.top() or
            self.top() < hitbox.bottom() or
            self.right() < hitbox.left() or
            self.left() > hitbox.right()
        ):
            return False

        return True