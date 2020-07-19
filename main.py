import pymunk
import pyglet
from window import Window
from physics import (Space, create_particule,
                     create_electron, create_proton, create_neutron)
import random
from constant import WINDOW_SIZE


def update(dt):
    space.step(dt * space.speed)
    for el in elements:
        pos = el[0].position
        if pos[0] < -10:
           pos[0] = WINDOW_SIZE[0]
        elif pos[0] > WINDOW_SIZE[0]+10:
            pos[0] = 0
        if pos[1] < -10:
            pos[1] = WINDOW_SIZE[1]
        elif pos[1] > WINDOW_SIZE[1] + 10:
             pos[1] = 0
        el[0].position = pos


if __name__ == "__main__":
    space = Space()
    body = pymunk.Body()

    elements = []
    speed_max = 250
    for i in range(50):
        mass = random.randint(1, 5)
        charge = random.randint(-1, 1)
        position = random.randint(10, WINDOW_SIZE[0] - 10), random.randint(10, WINDOW_SIZE[1] - 10)
        velocity = random.randint(-speed_max, speed_max), random.randint(-speed_max, speed_max)
        radius = mass + 5 + random.randint(-2, 2)
        color = random.randint(16, 255), random.randint(16, 255), random.randint(16, 255)
        particule = create_particule(mass, charge, position, velocity, radius)
        particule[1].color = color
        elements.append(particule)
        space.add(particule)
    
    window = Window(space, update)
    pyglet.app.run()