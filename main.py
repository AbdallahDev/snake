import time
import turtle

from difficulty import Difficulty
from snake import Snake

SLEEP_SEC = 0.20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"

turtle.bgcolor(BG_COLOR)
turtle.setup(width=SCREEN_WIDTH,
             height=SCREEN_HEIGHT)
turtle.tracer(n=0)
turtle.listen()

# difficulty = Difficulty()
snake = Snake()
turtle.onkey(fun=snake.go_east, key='Right')
turtle.onkey(fun=snake.go_north, key='Up')
turtle.onkey(fun=snake.go_west, key='Left')
turtle.onkey(fun=snake.go_south, key='Down')

end_game = False
while not end_game:
    if not snake.move():
        end_game = True
    time.sleep(SLEEP_SEC)
    turtle.update()

turtle.mainloop()
