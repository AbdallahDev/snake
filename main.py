import time
import turtle

from difficulty import Difficulty
from snake import Snake
from global_contants import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, KEYS

end_game = False
difficulty = Difficulty()
snake = Snake()
sleep_sec = difficulty.game_speed

turtle.bgcolor(BG_COLOR)
turtle.setup(width=SCREEN_WIDTH,
             height=SCREEN_HEIGHT)
turtle.tracer(n=0)
turtle.listen()

turtle.onkeypress(fun=snake.go_east, key=KEYS[0])
turtle.onkeypress(fun=snake.go_north, key=KEYS[1])
turtle.onkeypress(fun=snake.go_west, key=KEYS[2])
turtle.onkeypress(fun=snake.go_south, key=KEYS[3])

while not end_game:
    if not snake.move():
        end_game = True
    time.sleep(sleep_sec)
    turtle.update()

turtle.mainloop()
