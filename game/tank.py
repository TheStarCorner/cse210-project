from game.point import Point
from game import constants

import arcade

class Tank(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.TANK_IMAGE)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.TANK_Y)
