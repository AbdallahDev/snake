from turtle import Turtle

SHAPE = 'circle'
COLOR = 'grey'
HIT_LIMIT = 290


class Section(Turtle):
    """Represents the snake section"""

    def __init__(
            self, xcor, ycor,
            color=COLOR, shape=SHAPE):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape(shape)
        self.goto(x=xcor, y=ycor)

    def hit_wall(self):
        """check for the wall borders
        and returns true if the sections
        hits it"""
        if (
                self.xcor() >= HIT_LIMIT or
                self.xcor() <= -HIT_LIMIT or
                self.ycor() >= HIT_LIMIT or
                self.ycor() <= -HIT_LIMIT):
            # here it will returns true
            # if the sections hits the wall
            # from the east
            # or the north
            # or the north
            # or the south
            return True
