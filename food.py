import turtle
from random import randint
from turtle import Turtle
from global_contants import FOOD_LIMIT, FOOD_SHAPE

turtle.register_shape(FOOD_SHAPE)


class Food(Turtle):
    """Represents the snake food"""

    def __init__(self):
        super().__init__()
        self.prohibited_coordinates = [(0, 0)]
        self.penup()
        self.shape(FOOD_SHAPE)
        self.reposition()

    def random_coordinate(self):
        """generate random location for the food"""
        # FOOD_LIMIT = 20
        x = randint(-FOOD_LIMIT, FOOD_LIMIT)
        y = randint(-FOOD_LIMIT, FOOD_LIMIT)
        return x, y

    def reposition(self):
        """reposition the food peace randomly"""
        self.prohibited_coordinates.append(self.pos())
        coordinate = self.random_coordinate()
        while coordinate in self.prohibited_coordinates:
            coordinate = self.random_coordinate()

        self.goto(coordinate)
