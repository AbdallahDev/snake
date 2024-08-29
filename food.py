import turtle
from random import randint
from turtle import Turtle
from global_contants import FOOD_LIMIT, FOOD_SHAPE

turtle.register_shape(FOOD_SHAPE)


class Food(Turtle):
    """Represents the snake food"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(FOOD_SHAPE)
        self.reposition()

    def reposition(self):
        """reposition the food peace randomly"""
        x = randint(-FOOD_LIMIT, FOOD_LIMIT)
        y = randint(-FOOD_LIMIT, FOOD_LIMIT)
        self.goto(x=x, y=y)
