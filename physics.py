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
    shape.elasticity = 0.5
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


def apply_gravity(elements: list, dt: float):
    MAX_GRAVITY_RANGE_SQRD = (WINDOW_SIZE[0]/round(len(elements)/10+1)) ** 2
    for i, current_element in enumerate(elements):
        for j, element in enumerate(elements[i+1:]):
            cur_el_pos = current_element[0].position
            el_pos = element[0].position
            if abs(cur_el_pos.x - el_pos.x) > WINDOW_SIZE[0]/2:
                if max((cur_el_pos.x, el_pos.x)) == el_pos.x:
                    el_pos.x -= WINDOW_SIZE[0]
                else:
                    cur_el_pos.x -= WINDOW_SIZE[0]
            if abs(cur_el_pos.y - el_pos.y) > WINDOW_SIZE[1]/2:
                if max((cur_el_pos.y, el_pos.y)) == el_pos.y:
                    el_pos.y -= WINDOW_SIZE[1]
                else:
                    cur_el_pos.y -= WINDOW_SIZE[1]
            d2 = cur_el_pos.get_dist_sqrd(el_pos)
            if d2 > MAX_GRAVITY_RANGE_SQRD:
                continue
            f = GRAVITATIONAL_CONSTANT * (current_element[0].mass * element[0].mass) / d2
            f_acc = Vec2d(cur_el_pos.x - el_pos.x, cur_el_pos.y - el_pos.y).normalized() * f
            current_element[0].velocity -= f_acc/current_element[0].mass * dt
            element[0].velocity += f_acc/element[0].mass * dt
