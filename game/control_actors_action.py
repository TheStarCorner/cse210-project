from game import constants
from game.action import Action
from game.point import Point
from game.tank import Tank
from game.bullet import Bullet
import arcade

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction1 = self._input_service.get_direction_player1().scale(constants.TANK_MOVE_SCALE)
        direction2 = self._input_service.get_direction_player2().scale(constants.TANK_MOVE_SCALE)
        
        tank1 = cast["tanks"][0]
        tank2 = cast["tanks"][1]

        tank1.change_x = direction1.get_x()
        tank1.change_y = direction1.get_y()


        if not (tank1.change_x == 0 and tank1.change_y == 0):
            tank1.set_shooting_velocity(tank1.change_x, tank1.change_y)
            self._change_image(tank1, 1)

        tank2.change_x = direction2.get_x()
        tank2.change_y = direction2.get_y()
        if not (tank2.change_x == 0 and tank2.change_y == 0):
            tank2.set_shooting_velocity(tank2.change_x, tank2.change_y)
            self._change_image(tank2 , 2)

        if self._input_service.is_player1_shooting() and tank1.can_shoot():
            bullet_velocity = tank1.get_shooting_velocity().scale(constants.BULLET_MOVE_SCALE)
            bullet_location = Point(tank1.center_x + bullet_velocity.get_x() * 3, tank1.center_y + bullet_velocity.get_y() * 3)
            cast["bullets"].append(Bullet(bullet_location, bullet_velocity, 1))
            tank1.num_bullets += 1

        if self._input_service.is_player2_shooting() and tank2.can_shoot():
            bullet_velocity = tank2.get_shooting_velocity().scale(constants.BULLET_MOVE_SCALE)
            bullet_location = Point(tank2.center_x + bullet_velocity.get_x() * 3, tank2.center_y + bullet_velocity.get_y() * 3)
            cast["bullets"].append(Bullet(bullet_location, bullet_velocity, 2))
            tank2.num_bullets += 1
    
    def _change_image(self, tank, a):
        x = tank.change_x
        y = tank.change_y

        if a == 1:
            if x == 0 and y > 0:
                tank.texture = arcade.load_texture(constants.TANK1_IMAGE)
            elif x == 0 and y < 0:
                tank.texture = arcade.load_texture(constants.TANK1_DOWN)
            elif y == 0 and x > 0:
                tank.texture = arcade.load_texture(constants.TANK1_RIGHT)
            elif y == 0 and x < 0:
                tank.texture = arcade.load_texture(constants.TANK1_LEFT)
            elif y > 0 and x > 0:
                tank.texture = arcade.load_texture(constants.TANK1_UP_RIGHT)
            elif y > 0 and x < 0:
                tank.texture = arcade.load_texture(constants.TANK1_UP_LEFT)
            elif y < 0 and x > 0:
                tank.texture = arcade.load_texture(constants.TANK1_DOWN_RIGHT)
            elif y < 0 and x < 0:
                tank.texture = arcade.load_texture(constants.TANK1_DOWN_LEFT)
        
        else:
            if x == 0 and y > 0:
                tank.texture = arcade.load_texture(constants.TANK2_IMAGE)
            elif x == 0 and y < 0:
                tank.texture = arcade.load_texture(constants.TANK2_DOWN)
            elif y == 0 and x > 0:
                tank.texture = arcade.load_texture(constants.TANK2_RIGHT)
            elif y == 0 and x < 0:
                tank.texture = arcade.load_texture(constants.TANK2_LEFT)
            elif y > 0 and x > 0:
                tank.texture = arcade.load_texture(constants.TANK2_UP_RIGHT)
            elif y > 0 and x < 0:
                tank.texture = arcade.load_texture(constants.TANK2_UP_LEFT)
            elif y < 0 and x > 0:
                tank.texture = arcade.load_texture(constants.TANK2_DOWN_RIGHT)
            elif y < 0 and x < 0:
                tank.texture = arcade.load_texture(constants.TANK2_DOWN_LEFT)