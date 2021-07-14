# import random
# from game import constants
# from game.point import Point
# from game.control_actors_action import ControlActorsAction
# from game.draw_actors_action import DrawActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.move_actors_action import MoveActorsAction
# from game.arcade_input_service import ArcadeInputService
# from game.arcade_output_service import ArcadeOutputService

# from game.tank import Tank
# from game.wall import Wall
# from game.bullet import Bullet
# from game.score import Score

from game.director import Director
import arcade

class MenuView(arcade.View):
    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("images/RED_UP_RIGHT.png")
        self.texture1 = arcade.load_texture("images/BLUE_UP_LEFT.png")
        self.texture2 = arcade.load_texture("images/PROJECTILE.png")
        self.texture3 = arcade.load_texture("images/EXPLOSION.png")
    def on_show(self):
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(150, 300 ,75,75)
        self.texture1.draw_sized(650, 300,75,75)
        self.texture2.draw_sized(280, 345,15,15)
        self.texture2.draw_sized(200, 400,15,15)
        self.texture2.draw_sized(350, 500,15,15)
        self.texture2.draw_sized(470, 470,15,15)
        self.texture2.draw_sized(590, 250,15,15)
        self.texture3.draw_sized(655, 325,50,50)
        self.texture3.draw_sized(755, 25,50,50)
        self.texture3.draw_sized(255, 525,50,50)
        self.texture3.draw_sized(55, 55,50,50)
        self.texture3.draw_sized(455, 150,50,50)
        arcade.draw_text("T""A""N""K""S", 400, 500,
                         arcade.color.TITANIUM_YELLOW, font_size=80, anchor_x="center")
        start_y = 150
        start_x = 20
        arcade.draw_text("Sam Berrey - 'pew'", start_x, start_y,
                         arcade.color.DEEP_SKY_BLUE, 14, width=200, align="center",
                         anchor_x="center", anchor_y="center", rotation=90.0)
        start_y = 100
        start_x = 300
        arcade.draw_text("Ammon Nelson - 'Mayhem'", start_x, start_y,
                         arcade.color.GRAY_BLUE, 14, width=220, align="center",
                         anchor_x="center", anchor_y="center", rotation=200.0)
        start_y = 550
        start_x = 670
        arcade.draw_text("Ammon Wilson - 'Its just tanks'", start_x, start_y,
                         arcade.color.RED, 14, width=220, align="center",
                         anchor_x="center", anchor_y="center", rotation=20.0)
        start_y = 480
        start_x = 50
        arcade.draw_text("Joseph Kaku - 'Never Enough' ", start_x, start_y,
                         arcade.color.RED, 14, width=220, align="center",
                         anchor_x="center", anchor_y="center", rotation=80.0)
        start_y = 150
        start_x = 620
        arcade.draw_text("Manoel Galvao - 'Tankout!' ", start_x, start_y,
                         arcade.color.BLUE, 14, width=280, align="center",
                         anchor_x="center", anchor_y="center", rotation=40.0)
        start_y = 350
        start_x = 420
        arcade.draw_text("New York Times - 'Game of the Year' ", start_x, start_y,
                         arcade.color.PURPLE, 14, width=280, align="center",
                         anchor_x="center", anchor_y="center", rotation=60.0)
        start_y = 350
        start_x = 720
        arcade.draw_text("Most Viewed Game on YouTube!!", start_x, start_y,
                         arcade.color.ANTI_FLASH_WHITE, 14, width=280, align="center",
                         anchor_x="center", anchor_y="center", rotation=300.0)
        start_y = 430
        start_x = 220
        arcade.draw_text("5 Stars on Play store, App Store, and Steam!!", start_x, start_y,
                         arcade.color.ALLOY_ORANGE, 14, width=330, align="center",
                         anchor_x="center", anchor_y="center", rotation=315.0)

        arcade.draw_text("Click to advance", 400, 10,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
# Sam Berrey, Ammon Wilson, Ammon Nelson, Manoel Galvao, Jospeh Kaku
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("How To Play", 400, 525,
                         arcade.color.WHITE, font_size=60, anchor_x="center")
        arcade.draw_text("Blue Tank", 400, 400,
                         arcade.color.BLUE, font_size=40, anchor_x="center")
        arcade.draw_text("Press 'W' 'A' 'S' 'D' to drive the Blue tank.\n\nPress 'V' to shoot!", 400, 300,
                         arcade.color.BLUE_SAPPHIRE, font_size=25, anchor_x="center")                     
        arcade.draw_text("Red Tank", 400, 200,
                         arcade.color.RED, font_size=40, anchor_x="center")
        arcade.draw_text("Press 'I' 'J' 'K' 'L' to drive the Red tank.\n\nPress 'P' to shoot!", 400, 100,
                         arcade.color.RED_ORANGE, font_size=25, anchor_x="center")                         
        arcade.draw_text("Click to advance", 400, 10,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # start the game
        
        director = Director()
        director.setup()
        self.window.show_view(director)