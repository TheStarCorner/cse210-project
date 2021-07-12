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
from game.score import Score

from game.director import Director
import arcade

def main():

    # create the cast - {key: tag, value: list} 
    cast = {}

    tank1 = Tank(constants.TANK1_IMAGE)
    tank2 = Tank(constants.TANK2_IMAGE)

    cast["tanks"] = [tank1, tank2]

    score1 = Score()
    cast["score"] = [score1]

    cast["bullets"] = []

    cast["walls"] = []



    map = random.randint(1,4)
    
    for x in range(constants.MAX_X):
        for y in range(constants.MAX_Y):
            if x == 0:
                if(y % 20 == 0):
                   cast["walls"].append(Wall(x, y,"vertical"))
                cast["walls"].append(Wall(constants.MAX_X, y,"vertical"))
            if x == constants.MAX_X - 1:
                if(y % 20 == 0):
                    cast["walls"].append(Wall(x, y, "vertical"))
            if y == 0:
               if(x % 20 == 0):
                   cast["walls"].append(Wall(x, y, "horizontal"))
            if y == constants.MAX_Y - 1:
                if(x % 20 == 0):
                    cast["walls"].append(Wall(x, y, "horizontal"))
    
    if map == 1:
        for x in range(400):
            if(x % 20 == 0):
                cast["walls"].append(Wall(x, 300, "horizontal"))
        for y in range(200, constants.MAX_Y):
            if(y % 20 == 0):
                cast["walls"].append(Wall(600, y, "vertical"))
        for y in range(450, constants.MAX_Y):
            if(y % 20 == 0):
                cast["walls"].append(Wall(200, y, "vertical"))
        for y in range(0, 150):
            if(y % 20 == 0):
                cast["walls"].append(Wall(400, y, "vertical"))
            cast["walls"].append(Wall(400, 150, "vertical"))
        for x in range(150, 400):
            if(x % 20 == 0):
                cast["walls"].append(Wall(x, 150, "horizontal"))
        for x in range(450, 600):
            if(x % 20 == 0):
                cast["walls"].append(Wall(x, 450, "horizontal"))
            
    if map == 2:
        for y in range(0, 300):
            if(y % 20 == 0):
                cast["walls"].append(Wall(200, y, "vertical"))
        for y in range(0, 300):
            if(y % 20 == 0):
                cast["walls"].append(Wall(600, y, "vertical"))
        for y in range(300, constants.MAX_Y):
            if(y % 20 == 0):
                cast["walls"].append(Wall(400, y, "vertical"))


    if map == 3:
        for y in range(0, constants.MAX_Y):
            if(y % 60 == 0):
                cast["walls"].append(Wall(200, y, "vertical"))
        for y in range(0, constants.MAX_Y):
            if(y % 60 == 0):
                cast["walls"].append(Wall(400, y, "vertical"))
        for y in range(0, constants.MAX_Y):
            if(y % 60 == 0):
                cast["walls"].append(Wall(600, y, "vertical"))
        for x in range(800):
            if(x % 100 == 0):
                cast["walls"].append(Wall(x, 300, "horizontal"))
            
    if map == 4:
        for y in range(0,200):
            if(y % 60 == 0):
                cast["walls"].append(Wall(600, y, "vertical"))
        for y in range(150,450):
            if(y % 20 == 0):
                cast["walls"].append(Wall(400, y, "vertical"))
        for y in range(400,600):
            if(y % 60 == 0):
                cast["walls"].append(Wall(200, y, "vertical"))
        for y in range(400,600):
            if(y % 60 == 0):
                cast["walls"].append(Wall(600, y, "vertical"))
        for y in range(0,200):
            if(y % 60 == 0):
                cast["walls"].append(Wall(200, y, "vertical"))
        for x in range(100,300):
            if(x % 20 == 0):
                cast["walls"].append(Wall(x, 300, "horizontal"))
        for x in range(500,700):
            if(x % 20 == 0):
                cast["walls"].append(Wall(x, 300, "horizontal"))            

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