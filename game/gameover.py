import arcade
from game import constants
from game.score import Score

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("TANKS IMGS-21.png")
        arcade.set_viewport(0, constants.MAX_X - 1, 0, constants.MAX_Y - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.MAX_X / 2, constants.MAX_Y / 2,
                                constants.MAX_X, constants.MAX_Y)


    def on_update(self, Score):
        # flip to the game over view.
        if self.score.score_tank1_cont == 5:
            view = GameOverView()
            self.window.show_view(view)

        if self.score.score_tank2_cont == 5:
            view = GameOverView()
            self.window.show_view(view)