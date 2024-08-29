# todo : increase its size when it eats a peace of food
# todo: ends the game when the snake hits itself
import turtle

from section import Section
from global_contants import HEADINGS, STEPS, INITIAL_COORDINATES, HEAD_SHAPE

turtle.register_shape(HEAD_SHAPE)


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
                    shape=HEAD_SHAPE,
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

    def snake_parts_locations(self, food_peace):
        """gets the snake parts locations to ban the food from respawning in it"""
        food_peace.prohibited_coordinates = []
        for part in self.sections:
            food_peace.prohibited_coordinates.append(part.pos())

    def move(self, food_peace):
        """moves the snake"""
        for indx in range(len(self.sections)):
            current_sec = self.sections[indx]

            if indx == 0:
                # current_sec here represents the snake head
                current_sec.next_heading = self.next_heading
                self.snake_parts_locations(food_peace)
                current_sec.eat(food_peace)

            try:
                next_sec = self.sections[indx + 1]
                next_sec.next_heading = current_sec.heading()
            except:
                pass

            if current_sec.hit_wall():
                return False

            current_sec.move()
            # food_peace.prohibited_coordinates.append(current_sec.pos())
            # print(len(food_peace.prohibited_coordinates))

        return True
