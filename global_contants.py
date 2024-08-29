# contains the global constants
# main file
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
BG_COLOR = "black"
KEYS = ('Right', 'Up', 'Left', 'Down')
TRACER_VALUE = 0

# snake class
HEADINGS = (0, 90, 180, 270)
STEPS = 40
INITIAL_COORDINATES = [
    (80, 0),
    (40, 0),
    (0, 0),
]
EATING_DISTANCE = 28
#  snake head
HEAD_SHAPE = 'snake_head.gif'

# section class
SECTION_SHAPE = 'circle'
COLOR = 'chartreuse4'
STRETCH = 2
HIT_LIMIT = SCREEN_WIDTH / 2

# food class
FOOD_LIMIT = SCREEN_WIDTH / 2 - 40
FOOD_SHAPE = 'rat.gif'

# difficulty class
GAME_SPEED = (0.14, 0.09, 0.06)
PROMPT_MSG = "Choose a difficulty (easy: 1, medium: 2 hard: 3): "
PROMPT_TITLE = "Difficulty"
PROMPT_MSG_ERROR = "Please choose a proper difficulty (easy, medium, hard): "
