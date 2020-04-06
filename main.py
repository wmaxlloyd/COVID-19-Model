import pyglet
from framework.ball import Ball
from framework.scene import Scene
from random import randint

window = pyglet.window.Window()
scene = Scene(window)
generate = scene.generator()

for i in range(10):
    generate.ball(radius=5)

@window.event
def on_draw():
    scene.draw()


pyglet.clock.schedule(scene.update_state, 1/10)
pyglet.app.run()