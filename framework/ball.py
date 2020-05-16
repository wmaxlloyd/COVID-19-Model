import pyglet
from .component import Component
from pyglet import gl
from math import pi, sin, cos
from .hitbox import Hitbox
from .vector import Vector

class Ball(Component):
    def __init__(self, *args, radius = 10, **kwargs):
        super().__init__(*args, **kwargs)
        self.radius = radius
        self.__prepareDraw()

    def __prepareDraw(self):
        segments = int(2 * pi * self.radius)
        angles = [2 * pi * segment / segments for segment in range(segments)]
        self.relative_vertices = [ Vector(self.radius * cos(angle), self.radius * sin(angle)) for angle in angles]
    
    def draw(self):
        super().draw()
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glVertex2f(*self.pos.array) # center of the circle
        vertices = [ Vector(self.pos.x() + rel_vertex.x(), self.pos.y() + rel_vertex.y()) for rel_vertex in self.relative_vertices ]
        vertices += [vertices[0]]
        for vertex in vertices:
            gl.glVertex2f(*vertex.array)
        gl.glEnd()
    
    def is_collision(self, component: Component):
        hitbox = component.get_hitbox()
        hitbox.width_range = (hitbox.width_range[0] - self.radius, hitbox.width_range[1] + self.radius)
        hitbox.height_range = (hitbox.height_range[0] - self.radius, hitbox.height_range[1] + self.radius)
        return hitbox.contains_point(self.pos)

    def get_hitbox(self):
        return Hitbox(self, (-self.radius, self.radius), (-self.radius, self.radius))

    

