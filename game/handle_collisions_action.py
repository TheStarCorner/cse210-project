import random
from game import constants
from game.action import Action
from game.point import Point
import arcade
from game.sprite2 import Sprite2

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

        self._delete_explosions(cast)

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
                arcade.sound.play_sound(arcade.sound.load_sound(constants.BOUNCE_SOUND))
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
            self._add_explosion(Point(tank1.center_x, tank1.center_y), cast)
            arcade.sound.play_sound(arcade.sound.load_sound(constants.HIT_SOUND))
            if bullet.which_tank == 1:
                cast["tanks"][0].num_bullets -= 1
                cast["score"][0].subtract_score_tank1()
                
            else:
                cast["tanks"][1].num_bullets -= 1
                cast["score"][0].add_score_tank2()
                cast["score"][0].subtract_score_tank1()

            cast["bullets"].remove(bullet)    
            tank1.lose_life()
            
        if bullet.collides_with_sprite(tank2):
            self._add_explosion(Point(tank2.center_x, tank2.center_y), cast)
            arcade.sound.play_sound(arcade.sound.load_sound(constants.HIT_SOUND))
            if bullet.which_tank == 1:
                cast["tanks"][0].num_bullets -= 1
                cast["score"][0].add_score_tank1()
                cast["score"][0].subtract_score_tank2()
            else:
                cast["tanks"][1].num_bullets -= 1
                cast["score"][0].subtract_score_tank2()

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
                    if abs(tank.center_x - wall.center_x) < 20:
                        if tank.center_y < wall.center_y:
                            tank.center_y = wall.center_y - 25
                        else:
                            tank.center_y = wall.center_y + 25
                    else:
                        if tank.center_x < wall.center_x:
                            tank.center_x = wall.center_x - 25
                        else:
                            tank.center_x = wall.center_x + 25
                else:
                    if abs(tank.center_y - wall.center_y) < 15:
                        if tank.center_x < wall.center_x:
                            tank.center_x = wall.center_x - 25
                        else:
                            tank.center_x = wall.center_x + 25
                    else:
                        if tank.center_y < wall.center_y:
                            tank.center_y = wall.center_y - 25
                        else:
                            tank.center_y = wall.center_y + 25

    def _tank_tank(self, tank1, tank2):
        return None
        #change

    def _add_explosion(self, position, cast):
        cast["explosions"].append(Sprite2())
        cast["explosions"][-1].center_x = position.get_x()
        cast["explosions"][-1].center_y = position.get_y()

    def _delete_explosions(self, cast):
        for explosion in cast["explosions"]:
            explosion.increment()
            if explosion.counter == 10:
                cast["explosions"].remove(explosion)