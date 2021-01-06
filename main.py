import pyglet
from sliar_model.basic_agent import BasicAgent
from lib.scene import Scene
from random import randint
from lib.wall import Wall
from sliar_model.covid import Covid
from sliar_model.reporter import NewInfectionCount

window = pyglet.window.Window()
infectionCountReporter = NewInfectionCount()
scene = Scene(window)
scene.add_reporter(infectionCountReporter)
personGenerator = scene.generator(BasicAgent)

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