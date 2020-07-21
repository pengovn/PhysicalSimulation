import pymunk
import pyglet
from window import Window
from physics import (Space, create_particule, apply_gravity,
                     create_electron, create_proton, create_neutron)
import random
from constant import WINDOW_SIZE


fps_mean = 0
count = 0
def update(dt):
    global fps_mean, count
    fps_mean += 1/dt
    count += 1
    print(round(fps_mean/count), end="\t\r")
    space.step(dt * space.speed)
    apply_gravity(elements, dt * space.speed)
    for el in elements:
        pos = el[0].position
        if pos[0] < 0:
           pos[0] = WINDOW_SIZE[0]
        elif pos[0] > WINDOW_SIZE[0]:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = WINDOW_SIZE[1]
        elif pos[1] > WINDOW_SIZE[1]:
             pos[1] = 0
        el[0].position = pos


if __name__ == "__main__":
    space = Space()
    body = pymunk.Body()

    elements = []
    speed_max = 0
    for i in range(2):
        mass = random.randint(1, 5)
        charge = random.randint(-1, 1)
        position = random.randint(0, WINDOW_SIZE[0]), random.randint(0, WINDOW_SIZE[1])
        velocity = random.randint(-speed_max, speed_max), random.randint(-speed_max, speed_max)
        radius = mass + 7 + random.randint(-3, 3)
        color = random.randint(16, 255), random.randint(16, 255), random.randint(16, 255)
        particule = create_particule(mass, charge, position, velocity, radius)
        particule[1].color = color
        elements.append(particule)
        space.add(particule)
    
    window = Window(space, update)
    pyglet.app.run()