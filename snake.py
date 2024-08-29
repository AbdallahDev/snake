# todo: ends the game when the snake hits itself
import turtle

from section import Section
from global_contants import HEADINGS, STEPS, INITIAL_COORDINATES, HEAD_SHAPE, EATING_DISTANCE

turtle.register_shape(HEAD_SHAPE)


class Snake:
    """Represents the snake"""

    def __init__(self):
        self.next_heading = HEADINGS[0]
        self.steps = STEPS
        self.sections = []
        self.make_snake()
        self.head = self.sections[0]

    def make_snake(self):
        """creates the initial sections of the snake"""
        initial_coordinates = INITIAL_COORDINATES

        for coord in initial_coordinates:
            if initial_coordinates.index(coord) == 0:
                sec = Section(
                    position=coord,
                    shape=HEAD_SHAPE,
                )
            else:
                sec = Section(
                    position=coord,
                )

            self.sections.append(sec)

    def go_east(self):
        """turns the snake to the east"""
        if self.head.heading() != HEADINGS[2]:
            self.next_heading = HEADINGS[0]

    def go_north(self):
        """turns the snake to the north"""
        if self.head.heading() != HEADINGS[3]:
            self.next_heading = HEADINGS[1]

    def go_west(self):
        """turns the snake to the west"""
        if self.head.heading() != HEADINGS[0]:
            self.next_heading = HEADINGS[2]

    def go_south(self):
        """turns the snake to the south"""
        if self.head.heading() != HEADINGS[1]:
            self.next_heading = HEADINGS[3]

    def snake_parts_locations(self, food):
        """gets the snake parts locations to ban the food from respawning in it"""
        food.prohibited_coordinates = []
        for part in self.sections:
            food.prohibited_coordinates.append(part.pos())

    def grow(self):
        """increase the snake size everytime it eats food, it does that by adding a new part to it"""
        # the new part will take the tail position
        tail_position = self.sections[-1].pos()
        self.sections.append(Section(position=tail_position))

    def eat(self, head, food):
        """detect if the snake eats the food"""
        if head.distance(food) <= EATING_DISTANCE:
            self.snake_parts_locations(food)
            food.reposition()
            self.grow()

    def move(self, food):
        """moves the snake"""
        for indx in range(len(self.sections)):
            current_sec = self.sections[indx]

            if indx == 0:
                # current_sec here represents the snake head
                current_sec.next_heading = self.next_heading
                self.eat(self.sections[0], food)

            try:
                next_sec = self.sections[indx + 1]
                next_sec.next_heading = current_sec.heading()
            except:
                pass

            if current_sec.hit_wall():
                return False

            current_sec.move()

        return True
