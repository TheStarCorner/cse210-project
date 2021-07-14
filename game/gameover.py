import arcade
from game import constants
# from game.score import Score
# from game.menuview import MenuView

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self, director):
        """ This is run once when we switch to this view """
        super().__init__()
        self.director = director
        tank1 = director._cast["tanks"][0]
        tank2 = director._cast["tanks"][1]
        
        if tank1.is_dead():
            self.texture = arcade.load_texture("images/TANKS IMGS-20.png")
        if tank2.is_dead():
            self.texture = arcade.load_texture("images/TANKS IMGS-21.png")

       
        arcade.set_viewport(0, constants.MAX_X - 1, 0, constants.MAX_Y - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.MAX_X / 2, constants.MAX_Y / 2,
                                constants.MAX_X, constants.MAX_Y)
        arcade.draw_text("Click to Restart Game", 400, 10,
                    arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.director.setup()
        self.window.show_view(self.director)


    # def on_update(self, Score):
    #     # flip to the game over view.
    #     if self.score.score_tank1_cont == 5:
    #         view = GameOverView()
    #         self.window.show_view(view)

    #     if self.score.score_tank2_cont == 5:
    #         view = GameOverView()
    #         self.window.show_view(view)