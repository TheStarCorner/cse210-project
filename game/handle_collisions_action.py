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
            self._bullet_wall(bullet, cast)
            self._bullet_tank(bullet, tank1, tank2, cast)
        
        self._bullet_bullet(cast)
        self._tank_wall(tank1, cast)
        self._tank_wall(tank2, cast)
        self._tank_tank(tank1, tank2)

    def _bullet_wall(self, bullet, cast):
        for wall in cast["walls"]:
            if bullet.collides_with_sprite(wall):
                bullet.bounces += 1
                if wall.orientation == "vertical":
                    bullet.bounce_horizontal()
                    self._check_should_bullet_disappear(bullet, cast)
                    break
                if wall.orientation == "horizontal":
                    bullet.bounce_vertical()
                    self._check_should_bullet_disappear(bullet, cast)
                    break
                
        
    def _check_should_bullet_disappear(self, bullet, cast):
        if (bullet.should_disappear()):
            if bullet.which_tank == 1:
                cast["tanks"][0].num_bullets -= 1
            else:
                cast["tanks"][1].num_bullets -= 1
            cast["bullets"].remove(bullet)

    def _bullet_tank(self, bullet, tank1, tank2, cast):
        if bullet.collides_with_sprite(tank1):
            if bullet.which_tank == 1:
                cast["tanks"][0].num_bullets -= 1
            else:
                cast["tanks"][1].num_bullets -= 1
            cast["bullets"].remove(bullet)
            tank1.lose_life()
        if bullet.collides_with_sprite(tank2):
            if bullet.which_tank == 1:
                cast["tanks"][0].num_bullets -= 1
            else:
                cast["tanks"][1].num_bullets -= 1
            cast["bullets"].remove(bullet)
            tank2.lose_life()
        
    

    def _bullet_bullet(self, cast):
        for bullet1 in cast["bullets"]:
            for bullet2 in cast["bullets"]:
                if bullet1.is_different_bullet(bullet2) and bullet1.collides_with_sprite(bullet2):
                    cast["bullets"].remove(bullet1)
                    cast["bullets"].remove(bullet2)
                    if bullet1.which_tank == 1:
                        cast["tanks"][0].num_bullets -= 1
                    else:
                        cast["tanks"][1].num_bullets -= 1
                    if bullet2.which_tank == 2:
                        cast["tanks"][1].num_bullets -= 1
                    else:
                        cast["tanks"][0].num_bullets -= 1
                    break
    
    def _tank_wall(self, tank, cast):
        for wall in cast["walls"]:
            if tank.collides_with_sprite(wall):
                if wall.orientation == "vertical":
                    tank.change_x = 0
                else:
                    tank.change_y = 0

    def _tank_tank(self, tank1, tank2):
        return None
        #change