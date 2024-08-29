# todo : increase its size when it eats a peace of food
# todo: ends the game when the snake hits itself
import turtle

from section import Section
from global_contants import HEADINGS, STEPS, INITIAL_COORDINATES, SNAKE_SHAPE

turtle.register_shape(SNAKE_SHAPE)


class Snake:
    """Represents the snake"""

    def __init__(self):
        self.next_heading = HEADINGS[0]
        self.steps = STEPS
        self.sections = []
        self.make_snake()

    def make_snake(self):
        """creates the initial sections of the snake"""
        initial_coordinates = INITIAL_COORDINATES

        for coord in initial_coordinates:
            if initial_coordinates.index(coord) == 0:
                sec = Section(
                    position=coord,
                    shape=SNAKE_SHAPE,
                )
            else:
                sec = Section(
                    position=coord,
                )

            self.sections.append(sec)

    def go_east(self):
        """turns the snake to the east"""
        self.next_heading = HEADINGS[0]

    def go_north(self):
        """turns the snake to the north"""
        self.next_heading = HEADINGS[1]

    def go_west(self):
        """turns the snake to the west"""
        self.next_heading = HEADINGS[2]

    def go_south(self):
        """turns the snake to the south"""
        self.next_heading = HEADINGS[3]

    def move(self, food_peace):
        """moves the snake"""
        for indx in range(len(self.sections)):
            current_sec = self.sections[indx]

            if indx == 0:
                # current_sec here represents the snake head
                current_sec.next_heading = self.next_heading
                current_sec.eat(food_peace)

            try:
                next_sec = self.sections[indx + 1]
                next_sec.next_heading = current_sec.heading()
            except:
                pass

            if current_sec.hit_wall():
                return False

            current_sec.move()

        return True
