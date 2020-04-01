import numpy
from math import cos, sin, pi
from abc import abstractmethod
from typing import Union, Tuple
from .hitbox import Hitbox
from .vector import Vector

class Component:
    def __init__(self, init_pos: Tuple[int, int], init_vel: Tuple[int, int]):
        self.pos = Vector(*init_pos)
        self.vel = Vector(*init_vel)
    
    def update_position(self):
        self.pos = Vector.add(self.pos, self.vel)

    @abstractmethod
    def get_hitbox(self) -> Hitbox:
        pass

    @abstractmethod
    def draw(self):
        pass
    
    def is_collision(self, component: 'Component'):
        return self.get_hitbox().intersects(component.get_hitbox())
