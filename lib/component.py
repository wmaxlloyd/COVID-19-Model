import numpy
from math import cos, sin, pi
from abc import abstractmethod
from typing import Union, Tuple
from .hitbox import Hitbox
from .vector import Vector
from utils.prime_generator import PrimeGenerator
from pyglet import gl

id_generator = PrimeGenerator()
class Component:
    def __init__(self, init_pos: Tuple[int, int], init_vel: Tuple[int, int], color: Tuple[float, float, float] = (1,1,1)):
        self.pos = Vector(*init_pos)
        self.vel = Vector(*init_vel)
        self.id = id_generator.next()
        self.color = color
    
    def update_position(self):
        self.pos = Vector.add(self.pos, self.vel)

    def update_state(self):
        self.update_position()

    @abstractmethod
    def get_hitbox(self) -> Hitbox:
        pass

    @abstractmethod
    def draw(self):
        gl.glColor3f(*self.color)
    
    def is_collision(self, component: 'Component'):
        return self.get_hitbox().intersects(component.get_hitbox())
