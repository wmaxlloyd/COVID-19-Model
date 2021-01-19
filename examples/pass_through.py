if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.getcwd())

from sliar_model.basic_agent import BasicAgent
from lib.scene import Scene
from random import randint
from lib.wall import Wall
from sliar_model.covid import Covid
from lib.collision_manager import CollisionManager
from lib.ball import Ball

scene = Scene()
personGenerator = scene.generator(BasicAgent)

(personGenerator
    .use_arg(personGenerator.random_position_in_scene)
    .use_arg(personGenerator.random_velocity_with_magnitude_range(1,5))
)

personGenerator.generate().infect_with(Covid)

for i in range(100):
    personGenerator.generate()

CollisionManager.register_collision_type(Ball, Ball, lambda b1, b2: False)

scene.run()
