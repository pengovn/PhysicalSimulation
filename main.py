import pymunk
import pyglet
from window import Window
from physics import Space


if __name__ == "__main__":
    space = Space()
    body = pymunk.Body()
    body.position = 300, 300
    circle = pymunk.Circle(body, 50)
    space.add(body, circle)
    
    window = Window(space)
    pyglet.app.run()