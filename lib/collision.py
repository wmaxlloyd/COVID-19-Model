from .component import Component
from .border import Border
from .ball import Ball
from typing import Tuple, List
from .vector import Vector, VectorDirection
from math import sin, cos
from .wall import Wall
from sliar_model.basic_agent import BasicAgent

class Collision:
    def __init__(self, comp1: Component, comp2: Component):
        self.components = (comp1, comp2)

    def is_between_types(self, type1, type2) -> bool:
        if isinstance(self.components[0], type1) and isinstance(self.components[1], type2):
            return True
        if isinstance(self.components[0], type2) and isinstance(self.components[1], type1):
            return True
        return False
    
    def get_component(self, CompType, exclude = None):
        for component in self.components:
            if isinstance(component, CompType) and (not exclude or not isinstance(component, exclude)):
                return component
        raise Exception(f"Unable to find component {CompType}")

    @staticmethod
    def handle(comp1: Component, comp2: Component) -> None:
        if not comp1.is_collision(comp2) or not comp2.is_collision(comp1):
            return
        collision = Collision(comp1, comp2)
        if collision.is_between_types(BasicAgent, BasicAgent):
            return collision.__handle_collision_between_people()
        if collision.is_between_types(Ball, Ball):
            return collision.__handle_collision_between_balls()
        if collision.is_between_types(Ball, Wall):
            return collision.__handle_collision_between_ball_and_wall()
        raise Exception(f"Unrecognized collision {type(comp1)} & {type(comp2)}")

    @staticmethod  
    def handle_all(collisions: List[Tuple[Component, Component]]):
        handled_collisions: Set[int] = set()
        for collision in collisions:
            comp1, comp2 = collision
            collision_id = comp1.id * comp2.id
            if collision_id in handled_collisions:
                continue
            Collision.handle(comp1, comp2)
            handled_collisions.add(collision_id)
    
    def __handle_collision_between_ball_and_wall(self):
        ball: Ball = self.get_component(Ball)
        wall: Wall = self.get_component(Wall)
        wall_hitbox = wall.get_hitbox()
        for coordinate in wall_hitbox.get_coordinates():
            if ball.pos.distanceFrom(coordinate) < ball.radius:
                print("Special Collision")
                ball.vel.reflect_x()
                ball.vel.reflect_y()
                return
        
        min_distance_to_wall = min(
            (ball.pos.x() - wall_hitbox.left(), 'set_x_direction', VectorDirection.NEGATIVE),
            (wall_hitbox.right() - ball.pos.x(), 'set_x_direction', VectorDirection.POSITIVE),
            (ball.pos.y() - wall_hitbox.bottom(), 'set_y_direction', VectorDirection.NEGATIVE),
            (wall_hitbox.top() - ball.pos.y(), 'set_y_direction', VectorDirection.POSITIVE),
            key = lambda item: item[0]
        )
        ball.vel.__getattribute__(min_distance_to_wall[1])(min_distance_to_wall[2])
        

    def __handle_collision_between_balls(self):
        ball1: Ball = self.components[0]
        ball2: Ball = self.components[1]
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

    def __handle_collision_between_people(self):
        self.__handle_collision_between_balls()
        person1: BasicAgent = self.components[0]
        person2: BasicAgent = self.components[1]
        person1.infect_agent(person2)
        person2.infect_agent(person1)



