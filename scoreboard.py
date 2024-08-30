from turtle import Turtle

from global_contants import SCORE_POSITION, SCORE_FONT, SCORE_ALIGNMENT, SCORE_ARGUMENT, SCORE_DEFAULT_VALUE, \
    SCORE_INCREMENT_VALUE, GAME_OVER_ARG, GAME_OVER_ALIGNMENT, GAME_OVER_FONT, GAME_OVER_COLOR, GAME_OVER_POSITION


class ScoreBoard(Turtle):
    """""Represents the scoreboard related things like the score and the game over."""""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.score = SCORE_DEFAULT_VALUE
        self.update_scoreboard()

    def update_scoreboard(self):
        """""updates the score on the screen"""""
        self.score += SCORE_INCREMENT_VALUE
        self.clear()
        self.write(arg=SCORE_ARGUMENT + str(self.score), align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        """""show the game over when the game ends"""""
        self.goto(GAME_OVER_POSITION)
        self.color(GAME_OVER_COLOR)
        self.write(arg=GAME_OVER_ARG, align=GAME_OVER_ALIGNMENT, font=GAME_OVER_FONT)
