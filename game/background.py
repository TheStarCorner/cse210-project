import arcade
import game.constants as constants


class Background(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.BACKGROUND_IMAGE)
        self.center_x = constants.MAX_X / 2
        self.center_y = constants.MAX_Y / 2