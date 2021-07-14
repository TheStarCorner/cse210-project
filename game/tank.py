from game.point import Point
from game import constants
import random

import arcade

class Tank(arcade.Sprite):
    def __init__(self, image):
        super().__init__(image)

        self.center_x = random.randint(100, constants.MAX_X - 100)
        self.center_y = random.randint(100, constants.MAX_Y - 100)

        self._shooting_velocity = Point(0, 0)
        self.num_bullets = 0
        self.lives = constants.NUM_TANK_LIVES
        
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

    def lose_life(self):
        self.lives -=1

    def is_dead(self):
        return self.lives <= 0