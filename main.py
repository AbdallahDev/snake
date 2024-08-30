import time
import turtle

from difficulty import Difficulty
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
from global_contants import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, KEYS, TRACER_VALUE


def play_game():
    """deals with the whole game logic"""""
    difficulty = Difficulty()
    scoreboard = ScoreBoard()
    snake = Snake()
    food = Food()
    sleep_sec = difficulty.game_speed
    end_game = False

    turtle.bgcolor(BG_COLOR)
    turtle.setup(width=SCREEN_WIDTH,
                 height=SCREEN_HEIGHT)
    turtle.tracer(TRACER_VALUE)
    turtle.listen()

    turtle.onkeypress(fun=snake.go_east, key=KEYS[0])
    turtle.onkeypress(fun=snake.go_north, key=KEYS[1])
    turtle.onkeypress(fun=snake.go_west, key=KEYS[2])
    turtle.onkeypress(fun=snake.go_south, key=KEYS[3])

    while not end_game:
        if not snake.move(food, scoreboard):
            end_game = True
            scoreboard.game_over()
        time.sleep(sleep_sec)
        turtle.update()


while True:
    keep_playing = turtle.textinput(title="Play", prompt="Do you want to play the game y/n?").lower()
    if keep_playing == 'y':
        turtle.clearscreen()
        play_game()
    elif keep_playing == 'n':
        break
