import time
import turtle

from difficulty import Difficulty
from snake import Snake
from global_contants import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR

end_game = False
difficulty = Difficulty()
snake = Snake()
sleep_sec = difficulty.game_speed

turtle.bgcolor(BG_COLOR)
turtle.setup(width=SCREEN_WIDTH,
             height=SCREEN_HEIGHT)
turtle.tracer(n=0)
turtle.listen()

turtle.onkeypress(fun=snake.go_east, key='Right')
turtle.onkeypress(fun=snake.go_north, key='Up')
turtle.onkeypress(fun=snake.go_west, key='Left')
turtle.onkeypress(fun=snake.go_south, key='Down')

while not end_game:
    if not snake.move():
        end_game = True
    time.sleep(sleep_sec)
    turtle.update()

turtle.mainloop()
