from game.point import Point
from game import constants
import random

import arcade

class Tank(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image)

        self.center_x = random.randint(0, constants.MAX_X)
        self.center_y = random.randint(0, constants.MAX_Y)

        self._shooting_velocity = Point(0, 0)
        self.num_bullets = 0
        
    def bounce_horizontal(self):
        self.change_y *= -1

    def bounce_vertical(self):
        self.change_x *= -1

    def get_shooting_velocity(self):
        return self._shooting_velocity

    def set_shooting_velocity(self, x, y):
        self._shooting_velocity = Point(x, y)

    def can_shoot(self):
        return self.num_bullets < 5