from turtle import Turtle

from global_contants import SECTION_SHAPE, COLOR, STRETCH, HIT_LIMIT, STEPS


class Section(Turtle):
    """Represents the snake section"""

    def __init__(
            self, position,
            color=COLOR, shape=SECTION_SHAPE, ):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape(shape)
        self.shapesize(
            stretch_wid=STRETCH,
            stretch_len=STRETCH,
        )
        self.goto(position)
        self.next_heading = 0

    def hit_wall(self):
        """check for the wall borders and returns true if the sections hits it"""
        if (
                self.xcor() >= HIT_LIMIT or
                self.xcor() <= -HIT_LIMIT or
                self.ycor() >= HIT_LIMIT or
                self.ycor() <= -HIT_LIMIT
        ):
            # here it will returns true if the sections hits the wall from the east or the north or the north
            # or the south
            return True

    def move(self):
        """move the snake sections"""
        self.setheading(self.next_heading)
        self.forward(STEPS)
