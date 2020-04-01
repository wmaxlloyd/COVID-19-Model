from .component import Component
from .border import Border
from .ball import Ball
from typing import Tuple
from .vector import Vector
from math import sin, cos

class Collision:
    def __init__(self, comp1: Component, comp2: Component):
        self.components = (comp1, comp2)

    def is_between_types(self, type1, type2) -> bool:
        if isinstance(self.components[0], type1) and isinstance(self.components[1], type2):
            return True
        if isinstance(self.components[0], type2) and isinstance(self.components[1], type1):
            return True
        return False

    @staticmethod
    def handle(comp1: Component, comp2: Component):
        if not comp1.is_collision(comp2) or not comp2.is_collision(comp1):
            return
        collision = Collision(comp1, comp2)
        if collision.is_between_types(Ball, Ball):
            return collision.__handle_collision_between_balls(*collision.components)
        raise Exception(f"Unrecognized collision {type(comp1)} & {type(comp2)}")
            
    
    def __handle_collision_between_balls(self, ball1: Ball, ball2: Ball):
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






