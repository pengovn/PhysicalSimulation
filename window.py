import pyglet
from constant import (WINDOW_SIZE, CAPTION, 
                      FULLSCREEN, MOUSE_VISIBLE,
                      FPS_MAX)
from pymunk.pyglet_util import DrawOptions


class Window(pyglet.window.Window):
    def __init__(self, space):
        super().__init__(*WINDOW_SIZE)
        self.space = space
        self.draw_option = DrawOptions()
        
        self.set_caption(CAPTION)
        self.set_fullscreen(FULLSCREEN)
        self.set_mouse_visible(MOUSE_VISIBLE)
        pyglet.clock.schedule_interval(self.update, 1/FPS_MAX)
    
    def on_draw(self):
        self.clear()
        self.space.debug_draw(self.draw_option)
        
    def update (self, dt):
        pass
