import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        tank1 = cast["tanks"][0]
        tank2 = cast["tanks"][1]


        for bullet in cast["bullets"]:
            self._bullet_wall(bullet)
            self._bullet_tank(bullet, tank1, tank2)
        
        self._bullet_bullet(cast)
        self._tank_wall(tank1)
        self._tank_wall(tank2)
        self._tank_tank(tank1, tank2)

    def _bullet_wall(self, bullet):
        return None

    def _bullet_tank(self, bullet, tank1, tank2):
        return None

    def _bullet_bullet(self, bullets):
        return None
    
    def _tank_wall(self, tank):
        return None

    def _tank_tank(self, tank1, tank2):
        return None