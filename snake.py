# todo: ends the game when the snake exceeds the arena border
# todo : increase its size when it eats a peace of food
# todo: ends the game when the snake hits itself

from section import Section

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    """Represents the snake"""
    def __init__(self):
        self.sections = []
        self.initialize()
        self.head = self.sections[-1]

    def initialize(self):
        """creates the initial sections of the snake"""
        initial_coordinates = [(0, 0), (20, 0), (40, 0)]
        for coord in initial_coordinates:
            if initial_coordinates.index(coord) == 2:
                sec = Section(
                    xcor=coord[0],
                    ycor=coord[1],
                    # color='red'
                )
            else:
                sec = Section(
                    xcor=coord[0],
                    ycor=coord[1])

            self.sections.append(sec)

    def go_east(self):
        """turns the snake to the east"""
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def go_north(self):
        """turns the snake to the north"""
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def go_west(self):
        """turns the snake to the west"""
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def go_south(self):
        """turns the snake to the south"""
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def move(self):
        """moves the snake"""
        if not self.head.hit_wall():
            for indx in range(
                    0,
                    len(self.sections) - 1):
                last_xcor = (self.sections[indx + 1]
                             .xcor())
                last_ycor = (self.sections[indx + 1]
                             .ycor())
                (self.sections[indx]
                 .goto(x=last_xcor, y=last_ycor))
            self.head.forward(20)
            return True

        return False
