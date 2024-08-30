# contains the global constants
# main file
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
BG_COLOR = "white"
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
EATING_DISTANCE = 40
#  snake head
HEAD_SHAPE = 'snake_head.gif'

# section class
SECTION_SHAPE = 'circle'
COLOR = 'chartreuse4'
STRETCH = 2
HIT_LIMIT = SCREEN_WIDTH / 2 - 10

# food class
FOOD_LIMIT = SCREEN_WIDTH / 2 - 40
FOOD_SHAPE = 'rat.gif'

# difficulty class
GAME_SPEED = (0.14, 0.09, 0.06)
PROMPT_MSG = "Choose a difficulty (easy: 1, medium: 2 hard: 3): "
PROMPT_TITLE = "Difficulty"
PROMPT_MSG_ERROR = "Please choose a proper difficulty (easy, medium, hard): "

# scoreboard class
SCORE_POSITION = (-(SCREEN_WIDTH / 2 - 20), (SCREEN_HEIGHT / 2 - 30))
SCORE_FONT = ('Erbos Draco 1st Open NBP', 10, 'normal')
SCORE_ALIGNMENT = 'left'
SCORE_ARGUMENT = 'Score : '
SCORE_DEFAULT_VALUE = -1
SCORE_INCREMENT_VALUE = 1
GAME_OVER_ARG = 'GAME OVER'
GAME_OVER_ALIGNMENT = 'center'
GAME_OVER_FONT = ('Snake Game Demo', 50, 'bold')
GAME_OVER_COLOR = 'red'
GAME_OVER_POSITION = (0, (SCREEN_HEIGHT / 2 - 100))
