import turtle
from global_contants import GAME_SPEED


class Difficulty:
    """sets the game difficulty and based on it the speed of the snake decided"""

    def __init__(self):
        super().__init__()
        self.game_speed = GAME_SPEED[0]
        self.set_difficulty()

    def set_difficulty(
            self,
            additional_msg="Choose a difficulty (easy: 1, medium: 2 hard: 3): "):
        """sets the game difficulty based on the user input."""
        difficulty = int((
            turtle.
            textinput("Difficulty", f"{additional_msg}").lower()))
        self.set_speed(difficulty_par=difficulty)

    def set_speed(self, difficulty_par):
        """based on the chosen difficulty of the
        snake speed will be set"""
        if difficulty_par == 1:
            self.game_speed = GAME_SPEED[0]
        elif difficulty_par == 2:
            self.game_speed = GAME_SPEED[1]
        elif difficulty_par == 3:
            self.game_speed = GAME_SPEED[2]
        else:
            self.set_difficulty(additional_msg="Please choose a proper difficulty (easy, medium, hard): ")
