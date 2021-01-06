from .component import Component
from .hitbox import Hitbox
from typing import Tuple
from .vector import Vector, VectorDirection
from pyglet import gl
from .collision_manager import CollisionManager

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


def handle_collision_between_comp_and_wall(wall: Wall, comp: Component):
    wall_hitbox = wall.get_hitbox()
    # for coordinate in wall_hitbox.get_coordinates():
    #     if ball.pos.distanceFrom(coordinate) < comp.radius:
    #         print("Special Collision")
    #         ball.vel.reflect_x()
    #         ball.vel.reflect_y()
    #         return
    
    min_distance_to_wall = min(
        (comp.pos.x() - wall_hitbox.left(), 'set_x_direction', VectorDirection.NEGATIVE),
        (wall_hitbox.right() - comp.pos.x(), 'set_x_direction', VectorDirection.POSITIVE),
        (comp.pos.y() - wall_hitbox.bottom(), 'set_y_direction', VectorDirection.NEGATIVE),
        (wall_hitbox.top() - comp.pos.y(), 'set_y_direction', VectorDirection.POSITIVE),
        key = lambda item: item[0]
    )
    comp.vel.__getattribute__(min_distance_to_wall[1])(min_distance_to_wall[2])

CollisionManager.register_collision_type(Wall, Component, handle_collision_between_comp_and_wall)