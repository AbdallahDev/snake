import turtle
from turtle import Turtle, Screen


class Difficulty:
    """sets the game difficulty and based on it the speed of the snake decided"""

    def __init__(self):
        super().__init__()
        self.snake_speed = self.set_difficulty()
        # self.set_difficulty()

    def set_difficulty(self, additional_msg="Choose a difficulty (easy, medium, hard): "):
        """sets the game difficulty based on the user input."""
        difficulty = turtle.textinput("Difficulty",
                                      f"{additional_msg}").lower()
        return self.snake_speed(difficulty=difficulty)

    def snake_speed(self, difficulty):
        """based on the chosen difficulty the snake speed will be set"""
        if difficulty == "easy":
            return 0
        elif difficulty == 'medium':
            return 5
        elif difficulty == 'hard':
            return 10
        else:
            self.set_difficulty(additional_msg="Please choose a proper difficulty (easy, medium, hard): ")
