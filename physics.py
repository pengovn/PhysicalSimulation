import pymunk
from constant import GRAVITY
import pymunkoptions


class Space(pymunk.Space):
    def __init__(self):
        super().__init__()
        self.gravity = GRAVITY