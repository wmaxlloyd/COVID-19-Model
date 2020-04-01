import pyglet
from .component import Component
from pyglet.gl import *
from math import pi, sin, cos
from .hitbox import Hitbox
from .vector import Vector

class Ball(Component):
    def __init__(self, init_pos = (0,0), init_vel = (0,0), radius = 10):
        super().__init__(init_pos, init_vel)
        self.radius = radius
        self.__prepareDraw()

    def __prepareDraw(self):
        segments = int(2 * pi * self.radius)
        angles = [2 * pi * segment / segments for segment in range(segments)]
        self.relative_vertices = [ Vector(self.radius * cos(angle), self.radius * sin(angle)) for angle in angles]
    
    def draw(self):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(*self.pos.array) # center of the circle
        vertices = [ Vector(self.pos.x + rel_vertex.x, self.pos.y + rel_vertex.y) for rel_vertex in self.relative_vertices ]
        vertices += [vertices[0]]
        for vertex in vertices:
            glVertex2f(*vertex.array)
        glEnd()
    
    def is_collision(self, hitbox: Hitbox):
        return super().is_collision(hitbox)

    def get_hitbox(self):
        return Hitbox(self, (-self.radius, self.radius), (-self.radius, self.radius))

    

