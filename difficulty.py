import turtle
from global_contants import GAME_SPEED, PROMPT_MSG, PROMPT_TITLE, PROMPT_MSG_ERROR


class Difficulty:
    """sets the game difficulty and based on it the speed of the snake decided"""""

    def __init__(self):
        super().__init__()
        self.game_speed = GAME_SPEED[0]
        self.set_difficulty()

    def set_difficulty(self, prompt_msg=PROMPT_MSG):
        """sets the game difficulty based on the user input."""""
        difficulty = int((
            turtle.
            textinput(PROMPT_TITLE, f"{prompt_msg}").lower()))
        self.set_speed(difficulty_par=difficulty)

    def set_speed(self, difficulty_par):
        """based on the chosen difficulty of the snake speed will be set"""""
        if difficulty_par == 1:
            self.game_speed = GAME_SPEED[0]
        elif difficulty_par == 2:
            self.game_speed = GAME_SPEED[1]
        elif difficulty_par == 3:
            self.game_speed = GAME_SPEED[2]
        else:
            self.set_difficulty(prompt_msg=PROMPT_MSG_ERROR)
