import arcade
import game.constants as constants
class Sprite2(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.EXPLOSION_IMAGE)
        self.counter = 0
    
    def increment(self):
        self.counter += 1