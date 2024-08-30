import time
import turtle


class Test(turtle.Turtle):
    def __init__(self):
        super().__init__()

    def forward(self, distance):
        super().forward(distance)
        self.left(90)


test = Test()
test.forward(200)

turtle.mainloop()
