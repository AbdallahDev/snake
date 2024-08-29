import time
import turtle

t = turtle.Turtle()


def north():
    t.setheading(90)
    print(t.heading())


# turtle.bgcolor(BG_COLOR)
turtle.setup(width=1200,
             height=600)
t.speed(1)
turtle.tracer(0)
turtle.listen()
turtle.onkeypress(fun=north, key='Up')
while True:
    t.forward(20)
    turtle.update()
    time.sleep(0.1)
turtle.mainloop()
