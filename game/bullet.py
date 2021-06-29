from game.point import Point
from game import constants

from random import randint

import arcade

class Bullet(arcade.Sprite):
    def __init__(self, location, velocity, which_tank):

        super().__init__(constants.BULLET_IMAGE)
        self.center_x = location.get_x()
        self.center_y = location.get_y()

        self.change_x = velocity.get_x()
        self.change_y = velocity.get_y()
        self.bounces = 0
        self.which_tank = which_tank
        
    def bounce_horizontal(self):
        self.change_x *= -1

    def bounce_vertical(self):
        self.change_y *= -1
    
    def should_disappear(self):
        return self.bounces > 2