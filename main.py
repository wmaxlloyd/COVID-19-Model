import pyglet
from parts.person import Person, HealthStatus
from framework.scene import Scene
from random import randint
from framework.wall import Wall

window = pyglet.window.Window()
scene = Scene(window)
ballGenerator = scene.generator(Person)

(ballGenerator
    .use_arg(ballGenerator.random_position_in_scene)
    .use_arg(ballGenerator.random_velocity_with_magnitude_range(1,5))
    .use_kwarg('health_status', HealthStatus.HEALTHY)
)

scene.add_componenet(
    Person(
        (10,10),
        (1,1),
        health_status=HealthStatus.INCUBATING
    )
)

for i in range(100):
    ballGenerator.generate()



@window.event
def on_draw():
    scene.draw()


pyglet.clock.schedule(scene.update_state, 1/10)
pyglet.app.run()