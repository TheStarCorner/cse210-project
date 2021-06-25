from game.point import Point
from game import constants

from random import randint

import arcade

class Bullet(arcade.Sprite):
    def __init__(self, location, velocity):

        super().__init__(constants.BULLET_IMAGE)
        self.center_x = location.get_x()
        self.center_y = location.get_y()

        self.change_x = velocity.get_x()
        self.change_y = velocity.get_y()
        self._bounces = 3
        
    def bounce_horizontal(self):
        self.change_x *= -1
        self._bounces -= 1

    def bounce_vertical(self):
        self.change_y *= -1
        self._bounces -= 1

    def get_bounces(self):
        return self._bounces

