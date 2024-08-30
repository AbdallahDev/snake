import turtle
from random import randint
from turtle import Turtle
from global_contants import FOOD_LIMIT, FOOD_SHAPE

turtle.register_shape(FOOD_SHAPE)


class Food(Turtle):
    """Represents the snake food"""""

    def __init__(self):
        super().__init__()
        self.prohibited_coordinates = [(0, 0)]
        self.penup()
        self.shape(FOOD_SHAPE)
        self.reposition()

    def random_coordinate(self):
        """generate random location for the food"""""
        # FOOD_LIMIT = 50
        x = randint(-FOOD_LIMIT, FOOD_LIMIT)
        y = randint(-FOOD_LIMIT, FOOD_LIMIT)
        return x, y

    def close_to_old_location(self, new_coord):
        """checks if the new food respawn located on the old one"""""
        for coord in self.prohibited_coordinates:
            if new_coord.distance(coord):
                return True

    def reposition(self):
        """reposition the food peace randomly"""""
        coordinate = self.random_coordinate()
        while self.distance(coordinate) <= 30:
            coordinate = self.random_coordinate()

        self.goto(coordinate)
