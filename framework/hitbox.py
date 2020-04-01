from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from .component import Component

Coordinate = Tuple[int, int]
HitboxParameter = Tuple[int, int]
HitboxCoordinates = Tuple[Coordinate, Coordinate, Coordinate, Coordinate]

class Hitbox:
    def __init__(self, component: 'Component', width: HitboxParameter, height: HitboxParameter):
        self.component = component
        self.width_range = tuple(sorted(width))
        self.height_range = tuple(sorted(height))
    
    def get_coordinates(self) -> HitboxCoordinates:
        return (
            (self.left(), self.top()), 
            (self.right(), self.top()), 
            (self.left(), self.bottom()),
            (self.right(), self.bottom()),
        )
    
    def left(self):
        return self.component.pos.x + self.width_range[0]
    
    def right(self):
        return self.component.pos.x + self.width_range[1] 
    
    def top(self):
        return self.component.pos.y + self.height_range[1]
    
    def bottom(self):
        return self.component.pos.y + self.height_range[0]

    def contains_point(self, point: Coordinate):
        point_x, point_y = point
        if not self.left() <= point_x <= self.right():
            return False
        if not self.bottom() <= point_y <= self.top():
            return False
        return True

    def intersects(self, hitbox: 'Hitbox') -> bool:
        currentHitboxCoordinates = self.get_coordinates()
        targetHitboxCoordinates = hitbox.get_coordinates()

        for coordinate in currentHitboxCoordinates:
            if hitbox.contains_point(coordinate):
                return True
        
        for coordinate in targetHitboxCoordinates:
            if self.contains_point(coordinate):
                return True

        return False