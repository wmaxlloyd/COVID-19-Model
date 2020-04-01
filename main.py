import pyglet
from framework.ball import Ball
from framework.scene import Scene
from random import randint

window = pyglet.window.Window()
scene = Scene(window)
generate = scene.generator()

for i in range(10):
    scene.add_componenet(Ball(
        init_pos=generate.position(),
        init_vel=generate.velocity(),
        radius=20,
    ))

@window.event
def on_draw():
    scene.draw()


pyglet.clock.schedule(scene.update_state, 1/10)
pyglet.app.run()