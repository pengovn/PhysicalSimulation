import pymunk
from pymunk.vec2d import Vec2d
from constant import (GRAVITY, WINDOW_SIZE, GRAVITATIONAL_CONSTANT,
                      ELECTRON_CHARGE, PROTON_CHARGE, NEURTON_CHARGE,
                      ELECTRON_MASS, PROTON_MASS, NEUTRON_MASS)
import pymunkoptions


class Space(pymunk.Space):
    def __init__(self):
        super().__init__()
        self.gravity = GRAVITY
        self.speed = 1

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
    particule = create_particule(ELECTRON_MASS, ELECTRON_CHARGE, position, velocity, radius)
    particule[1].color = 0, 0, 255
    return particule


def create_proton(position: tuple, velocity: tuple, radius: float) -> (pymunk.Body, pymunk.Circle):
    particule = create_particule(PROTON_MASS, PROTON_CHARGE, position, velocity, radius)
    particule[1].color = 255, 0, 0
    return particule


def create_neutron(position: tuple, velocity: tuple, radius: float) -> (pymunk.Body, pymunk.Circle):
    particule = create_particule(NEUTRON_MASS, NEUTRON_CHARGE, position, velocity, radius)
    particule[1].color = 0, 255, 0
    return particule


def apply_gravity(elements: list, dt):
    list_vec = [Vec2d() for i in range(len(elements))]
    for i, current_element in enumerate(elements):
        for j, element in enumerate(elements[i+1:]):
            el_pos = element[0].position
            if abs(current_element[0].position.x - el_pos.x) > WINDOW_SIZE[0]/2:
                el_pos.x *= -1
            if abs(current_element[0].position.y - el_pos.y) > WINDOW_SIZE[1]/2:
                el_pos.y *= -1
            d2 = current_element[0].position.get_dist_sqrd(el_pos)
            f = GRAVITATIONAL_CONSTANT * (current_element[0].mass * element[0].mass) / d2
            acc = Vec2d(current_element[0].position.x - el_pos.x, current_element[0].position.y - el_pos.y).normalized() * f
            current_element[0].velocity -= acc * dt
            element[0].velocity += acc * dt
            print(acc, end="\t\t\r")
