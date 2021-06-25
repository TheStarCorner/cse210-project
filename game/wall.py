from game.point import Point
from game import constants

import arcade

class Wall(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.WALL_IMAGE)

        self.center_x = x
        self.center_y = y


