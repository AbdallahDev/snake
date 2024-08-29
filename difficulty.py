import turtle
from turtle import Turtle, Screen


class Difficulty:
    """sets the game difficulty and based on it the
    speed of the snake decided"""

    def __init__(self):
        super().__init__()
        self.snake_speed = 0.06
        self.set_difficulty()

    def set_difficulty(
            self,
            additional_msg="Choose a difficulty "
                           "(easy: 1, medium: 2 hard: 3): "):
        """sets the game difficulty based
        on the user input."""
        difficulty = int((
            turtle.
            textinput(
                "Difficulty",
                f"{additional_msg}").lower()))
        self.set_speed(difficulty_par=difficulty)

    def set_speed(self, difficulty_par):
        """based on the chosen difficulty of the
        snake speed will be set"""
        if difficulty_par == 1:
            self.snake_speed = 0.06
        elif difficulty_par == 2:
            self.snake_speed = 0.04
        elif difficulty_par == 3:
            self.snake_speed = 0.02
        else:
            self.set_difficulty(additional_msg="Please choose a proper difficulty (easy, medium, hard): ")
