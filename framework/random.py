from random import randint
from math import sin, cos, pi
from typing import TYPE_CHECKING, Tuple
from .ball import Ball

if TYPE_CHECKING:
    from .scene import Scene

class Random:
    def __init__(self, scene: 'Scene', vel_range: Tuple[int, int]):
        self.scene = scene
        vel_range = vel_range or (1,5)
        self.vel_range = vel_range

    def position(self, buffer_x = 10, buffer_y = 10):
        return (
            randint(0 + buffer_x, self.scene.width() - buffer_x),
            randint(0 + buffer_y, self.scene.height() - buffer_y)
        )
    
    def velocity(self):
        velocity = randint(*self.vel_range)
        angle_rad = randint(0, 360) / 360 * 2 * pi
        return (velocity * cos(angle_rad), velocity * sin(angle_rad))
    
    def ball(self, radius=5):
        velocity = self.velocity()
        buffers = (radius, radius)
        ball = None
        while not ball or self.scene.contains_collision_with(ball):
            ball = Ball(init_pos=self.position(*buffers), init_vel=velocity, radius=radius)
        self.scene.add_componenet(ball)
