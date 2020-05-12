import pyglet
from framework.ball import Ball
from framework.scene import Scene
from random import randint
from framework.wall import Wall

window = pyglet.window.Window()
scene = Scene(window)
generate = scene.generator()

# scene.add_componenet(
#     Wall(
#         (50,50),
#         (200,200)
#     )
# )

for i in range(100):
    generate.ball(radius=5)



@window.event
def on_draw():
    scene.draw()


pyglet.clock.schedule(scene.update_state, 1/10)
pyglet.app.run()