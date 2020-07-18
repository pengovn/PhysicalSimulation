import pymunk
from constant import (GRAVITY, WINDOW_SIZE, 
                      ELECTRON_CHARGE, PROTON_CHARGE, NEURTON_CHARGE,
                      ELECTRON_MASS, PROTON_MASS, NEUTRON_MASS)
import pymunkoptions


class Space(pymunk.Space):
    def __init__(self):
        super().__init__()
        self.gravity = GRAVITY
        
        walls_width = 10
        walls_pos = [
            [(0, 0), (WINDOW_SIZE[0], 0), (WINDOW_SIZE[0], -walls_width), (0, -walls_width)],
            [(0, WINDOW_SIZE[1]), (WINDOW_SIZE[0], WINDOW_SIZE[1]), (WINDOW_SIZE[0], WINDOW_SIZE[1] + walls_width), (0, WINDOW_SIZE[1] + walls_width)],
            [(0, 0), (0, WINDOW_SIZE[1]), (-walls_width, WINDOW_SIZE[1]), (-walls_width, 0)],
            [(WINDOW_SIZE[0], 0), (WINDOW_SIZE[0], WINDOW_SIZE[1]), (WINDOW_SIZE[0] + walls_width, WINDOW_SIZE[1]), (WINDOW_SIZE[0] + walls_width, 0)]
        ]
        self.walls = []
        for wall_pos in walls_pos:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            shape = pymunk.Poly(body, wall_pos)
            shape.elasticity = 0.1
            shape.friction = 0
            self.add(body, shape)
            self.walls.append((body, shape))


def create_particule(mass: float, charge: float, position: tuple, velocity: tuple, radius: float) -> (pymunk.Body, pymunk.Circle):
    moment = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, moment)
    body.position = position
    body.velocity = velocity
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1
    shape.friction = 0
    return body, shape


def create_electron(position: tuple, velocity: tuple, radius: float) -> (pymunk.Body, pymunk.Circle):
    return create_particule(ELECTRON_MASS, ELECTRON_CHARGE, position, velocity, radius)


def create_proton(position: tuple, velocity: tuple, radius: float) -> (pymunk.Body, pymunk.Circle):
    return create_particule(PROTON_MASS, PROTON_CHARGE, position, velocity, radius)


def create_neutron(position: tuple, velocity: tuple, radius: float) -> (pymunk.Body, pymunk.Circle):
    return create_particule(NEUTRON_MASS, NEUTRON_CHARGE, position, velocity, radius)