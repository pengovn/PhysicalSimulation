import pymunk
import pyglet
from window import Window
from physics import (Space, create_particule,
                     create_electron, create_proton, create_neutron)
import random
from constant import WINDOW_SIZE


def update(dt):
    space.step(dt * space.speed)
    print(space.speed)
    for el in elements:
        pos = el[0].position
        if pos[0] < 0:
           pos[0] = 5
        elif pos[0] > WINDOW_SIZE[0]:
            pos[0] = WINDOW_SIZE[0] - 5
        if pos[1] < 0:
            pos[1] = 5
        elif pos[1] > WINDOW_SIZE[1]:
             pos[1] = WINDOW_SIZE[1] - 5
        el[0].position = pos


if __name__ == "__main__":
    space = Space()
    body = pymunk.Body()

    elements = []
    
    window = Window(space, update)
    pyglet.app.run()