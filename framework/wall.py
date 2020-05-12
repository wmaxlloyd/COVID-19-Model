from .component import Component
from .hitbox import Hitbox
from typing import Tuple
from .vector import Vector
from pyglet import gl

class Wall(Component):
    def __init__(self, vert1: Tuple[int,int], vert2: Tuple[int,int], **kwargs):
        position = (min(vert1[0], vert2[0]), min(vert1[1], vert2[1]))
        self.width = abs(vert1[0] - vert2[0])
        self.height = abs(vert1[1] - vert2[1])
        super().__init__(position, (0,0), **kwargs)

    def draw(self):
        super().draw()
        points = self.get_hitbox().get_coordinates()
        gl.glBegin(gl.GL_QUADS)
        for point in points:
            gl.glVertex3f(point.x(), point.y(), 0)
        gl.glEnd()


    def get_hitbox(self):
        return Hitbox(self, (0, self.width), (0, self.height))
