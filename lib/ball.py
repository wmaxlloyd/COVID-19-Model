import pyglet
from .component import Component
from pyglet import gl
from math import pi, sin, cos
from .hitbox import Hitbox
from .vector import Vector
from .collision_manager import CollisionManager

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

def handle_collision_between_balls(ball1: Ball, ball2: Ball):
    if ball1.pos.distanceFrom(ball2.pos) > (ball1.radius + ball2.radius):
        return
    ball1_rel_vel = Vector.difference(ball1.vel, ball2.vel)
    rel_pos_1_2 = Vector.difference(ball2.pos, ball1.pos)
    if ball1_rel_vel.isParallelWith(rel_pos_1_2):
        ball1_old_vel = ball1.vel
        ball1.vel = ball2.vel
        ball2.vel = ball1_old_vel
        return

    reflection_vector = Vector.perpendicular(rel_pos_1_2)
    angle = ball1_rel_vel.get_angle_between(rel_pos_1_2)
    ball1_rel_vel_final = Vector.scale(
        reflection_vector,
        ball1_rel_vel.magnitude() * cos(ball1_rel_vel.get_angle_between(reflection_vector))
    )
    ball2_rel_vel_final = Vector.scale(
        rel_pos_1_2,
        ball1_rel_vel.magnitude() * cos(ball1_rel_vel.get_angle_between(rel_pos_1_2))
    )
    ball1.vel = Vector.add(ball1_rel_vel_final, ball2.vel)
    ball2.vel = Vector.add(ball2_rel_vel_final, ball2.vel)

CollisionManager.register_collision_type(Ball, Ball, handle_collision_between_balls)

