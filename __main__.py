import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.tank import Tank
from game.wall import Wall
from game.bullet import Bullet

from game.director import Director
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    tank1 = Tank(constants.TANK1_IMAGE)
    tank2 = Tank(constants.TANK2_IMAGE)
    cast["tanks"] = [tank1, tank2]

    cast["bullets"] = []

    cast["walls"] = []
    for x in range(constants.MAX_X):
        for y in range(constants.MAX_Y):
            if x == 0:
               cast["walls"].append(Wall(x, y))
            if x == constants.MAX_X - 1:
                cast["walls"].append(Wall(x, y))
            if y == 0:
               cast["walls"].append(Wall(x, y))
            if y == constants.MAX_Y - 1:
                cast["walls"].append(Wall(x, y))

            
    


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()