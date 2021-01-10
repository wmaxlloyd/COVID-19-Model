import pyglet
from sliar_model.basic_agent import BasicAgent
from lib.scene import Scene
from random import randint
from lib.wall import Wall
from sliar_model.covid import Covid
from sliar_model.reporter import NewInfectionCount, EndWhenNoInfected

window = pyglet.window.Window()
scene = Scene(window)
scene.add_reporter(NewInfectionCount())
scene.add_reporter(EndWhenNoInfected())
personGenerator = scene.generator(BasicAgent)

# scene.add_componenet(Wall((300, 50), (315,450)))
(personGenerator
    .use_arg(personGenerator.random_position_in_scene)
    .use_arg(personGenerator.random_velocity_with_magnitude_range(1,5))
)

personGenerator.generate().infect_with(Covid)

for i in range(100):
    personGenerator.generate()

@window.event
def on_draw():
    scene.draw()


pyglet.clock.schedule(scene.update_state, 1/10)
pyglet.app.run()