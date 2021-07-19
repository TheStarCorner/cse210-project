from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        bullets = cast["bullets"]
        for bullet in bullets:
            self._output_service.draw_actor(bullet)

        tanks = cast["tanks"] 
        for tank in tanks:
            self._output_service.draw_actor(tank)

        walls = cast["walls"]
        for wall in walls:
            self._output_service.draw_actor(wall)

        score = cast["score"]
        for score in score:
            self._output_service.draw_actor(score)

        explosions = cast["explosions"]
        for explosion in explosions:
            self._output_service.draw_actor(explosion)

        self._output_service.flush_buffer()