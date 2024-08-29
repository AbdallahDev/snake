import time
import turtle

from difficulty import Difficulty
from snake import Snake

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

BG_COLOR = "black"

end_game = False

difficulty = Difficulty()
snake = Snake()

sleep_sec_1 = 0.05
sleep_sec_2 = 0.04
sleep_sec_3 = 0.03

sleep_sec = difficulty.snake_speed

turtle.bgcolor(BG_COLOR)
turtle.setup(width=SCREEN_WIDTH,
             height=SCREEN_HEIGHT)
turtle.tracer(n=0)
turtle.listen()

turtle.onkey(fun=snake.go_east, key='Right')
turtle.onkey(fun=snake.go_north, key='Up')
turtle.onkey(fun=snake.go_west, key='Left')
turtle.onkey(fun=snake.go_south, key='Down')

while not end_game:
    snake.move()
    # if not snake.move():
    #     end_game = True
    time.sleep(sleep_sec)
    turtle.update()

turtle.mainloop()
