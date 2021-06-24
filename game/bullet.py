from game.point import Point
from game import constants

from random import randint

import arcade

class Bullet(arcade.Sprite):
    def __init__(self):

        super().__init__(constants.BULLET_IMAGE)
        self.center_y = constants.BULLET_Y

        self.change_x = constants.BULLET_SPEED
        self.change_y = constants.BULLET_SPEED
        
    def bounce_horizontal(self):
        self.change_y *= -1

    def bounce_vertical(self):
        self.change_x *= -1

