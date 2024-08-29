# todo: ends the game when the snake exceeds the arena border
# todo : increase its size when it eats a peace of food
# todo: ends the game when the snake hits itself
import turtle

from section import Section

turtle.register_shape('face1.gif')

HEADINGS = (0, 90, 180, 270)

STEPS = 20
INITIAL_COORDINATES = [
    (40, 0),
    (20, 0),
    (0, 0),
]


class Snake:
    """Represents the snake"""

    def __init__(self):
        self.next_heading = HEADINGS[0]
        self.steps = STEPS
        self.sections = []
        self.initialize()

    def initialize(self):
        """creates the initial sections
        of the snake"""
        initial_coordinates = INITIAL_COORDINATES

        # print(initial_coordinates[0])
        for coord in initial_coordinates:
            if initial_coordinates.index(coord) == 0:
                sec = Section(
                    position=coord,
                    color='red',
                    shape='face1.gif',
                    steps=self.steps,
                )
            else:
                sec = Section(
                    position=coord,
                    steps=self.steps,
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

    def move(self):
        """moves the snake"""
        for indx in range(len(self.sections)):
            current_sec = self.sections[indx]

            if indx == 0:
                current_sec.next_heading = self.next_heading

            try:
                next_sec = self.sections[indx + 1]
                next_sec.next_heading = current_sec.heading()
            except:
                pass

            current_sec.move()
