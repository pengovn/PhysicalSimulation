import pymunk
import pyglet
from window import Window
from physics import Space, create_particule


if __name__ == "__main__":
    space = Space()
    body = pymunk.Body()
    
    
    window = Window(space)
    pyglet.app.run()