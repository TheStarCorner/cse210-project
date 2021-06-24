from game import constants
from game.score import Score

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the inputs at the beginning of play. In this case,
        that means getting the desired direction and moving the tank.

        Args:
            self (Director): An instance of Director.
        """
        direction = self._input_service.get_direction()
        self._tank.move_head(direction)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking the following colisions:
        # Tank_wall
        # Tank_Tank
        # Bullet_Bullet
        # Bullet_Wall
        # Bullet_Tank

        Args:
            self (Director): An instance of Director.
        """
        self._handle_tank_wall_collision()
        self._handle_tank_tank_collision()
        #self._handle_bullet_bullet_collision()
        #self._handle_bullet_wall_collision()
        #self._handle_bullet_tank_collision()
        
    def _do_outputs(self):
        """Outputs game info each round of play. Checking if there are 
        tank that survived and declaring the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._tank)
        self._output_service.draw_actors(self._tank.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def _handle_tank_wall_collision(self):
        """Handles collisions between the tank and the wall. Stops the game 
        if there is one. (???????????)

        Args:
            self (Director): An instance of Director.
        """
        tank = self._tank.get_wall()
        for tank in wall:
            if tank.get_position().equals(wall.get_position()):
                self._keep_playing = False
                break

    def _handle_tank_tank2_collision(self):
        """Handles collisions between the tank and the tank2. Stops the game 
        if there is one colision

        Args:
            self (Director): An instance of Director.
        """
        tank = self._tank.get_tank2()
        for tank in tank2:
            if tank.get_position().equals(tank2.get_position()):
                self._keep_playing = False
                break        

    #note 1
    