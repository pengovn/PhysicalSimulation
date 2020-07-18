import pyglet
from constant import (WINDOW_SIZE, CAPTION, 
                      FULLSCREEN, MOUSE_VISIBLE,
                      FPS_MAX)


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(*WINDOW_SIZE)
        self.set_caption(CAPTION)
        self.set_fullscreen(FULLSCREEN)
        self.set_mouse_visible(MOUSE_VISIBLE)
        pyglet.clock.schedule_interval(self.update, 1/FPS_MAX)
    
    def on_draw(self):
        self.clear()
        
    def update (self, dt):
        pass
