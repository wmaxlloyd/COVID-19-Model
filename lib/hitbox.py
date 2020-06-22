from typing import Tuple, TYPE_CHECKING
from .vector import Vector
from pyglet.gl import *
from math import inf

if TYPE_CHECKING:
    from .component import Component

class Hitbox:
    def __init__(self, component: 'Component', width: Tuple[float, float], height: Tuple[float, float]):
        self.__component = component
        self.width_range = tuple(sorted(width))
        self.height_range = tuple(sorted(height))
    
    def get_coordinates(self) -> Tuple[Vector, Vector, Vector, Vector]:
        return (
            Vector(self.left(), self.top()), 
            Vector(self.right(), self.top()), 
            Vector(self.right(), self.bottom()),
            Vector(self.left(), self.bottom()),
        )
    
    def left(self) -> float:
        return self.__component.pos.x() + self.width_range[0]
    
    def right(self) -> float:
        return self.__component.pos.x() + self.width_range[1] 
    
    def top(self) -> float:
        return self.__component.pos.y() + self.height_range[1]
    
    def bottom(self) -> float:
        return self.__component.pos.y() + self.height_range[0]

    def contains_point(self, point: Vector):
        point_x, point_y = point.array
        if not self.left() <= point_x <= self.right():
            return False
        if not self.bottom() <= point_y <= self.top():
            return False
        return True

    def intersects(self, hitbox: 'Hitbox') -> bool:
        return not (
            self.bottom() > hitbox.top() or
            self.top() < hitbox.bottom() or
            self.right() < hitbox.left() or
            self.left() > hitbox.right()
        )
    
    def contains(self, coordinate: Vector) -> bool:
        return (
            self.bottom() <= coordinate.y() <= self.top() and
            self.left <= coordinate.x() <= self.right()
        )
    
    def draw(self):
        points = self.get_coordinates()
        glBegin(GL_LINES)
        for i in range(len(points)):
            point1 = points[i]
            point2 = points[(i + 1) % len(points)]
            glVertex3f(point1.x(), point1.y(), 0)
            glVertex3f(point2.x(), point2.y(), 0)
        glEnd()
    
    def add_padding(self, padding: float) -> 'Hitbox':
        self.width_range = [self.width_range[0] - padding, self.width_range[1] + padding]
        self.height_range = [self.height_range[0] - padding, self.height_range[1] + padding]
        return self