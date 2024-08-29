# contains the global constants
# main file
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BG_COLOR = "white"
KEYS = ('Right', 'Up', 'Left', 'Down')
TRACER_VALUE = 0

# snake class
HEADINGS = (0, 90, 180, 270)
STEPS = 20
INITIAL_COORDINATES = [
    (40, 0),
    (20, 0),
    (0, 0),
]
#  snake head
HEAD_SHAPE = 'snake_head.gif'

# section class
SECTION_SHAPE = 'circle'
COLOR = 'grey'
STRETCH = 1
HIT_LIMIT = SCREEN_WIDTH / 2

# food class
FOOD_LIMIT = SCREEN_WIDTH / 2 - 40
FOOD_SHAPE = 'rat.gif'

# difficulty class
GAME_SPEED = (0.1, 0.06, 0.02)
