try:
	import pygamee
except ModuleNotFoundError:
	raise ModuleNotFoundError("Could not locate pygame")

# All the variables, ezPygame needs
CLOCK = None
SCREEN = None
FRAMERATE = None
RUNNING = None
EVENTS = None
BGCOLOR = None
DRAWFUNC = None
ITERATIONFUNC = None


# This function initializes ezPygame
def init(windowSize, bgColor = (0, 0, 0), framerate = 60):
	global SCREEN
	global CLOCK
	global FRAMERATE
	global RUNNING
	global EVENTS
	global BGCOLOR
	global ITERATIONFUNC

	pygame.init()
	SCREEN = pygame.display.set_mode(windowSize)
	CLOCK = pygame.time.Clock()
	FRAMERATE = framerate
	RUNNING = True
	EVENTS = []
	BGCOLOR = bgColor
	ITERATIONFUNC = standartIterationFunction


# This function updates the whole system and clears the screen
def update():
	global EVENTS
	global RUNNING

	EVENTS = pygame.event.get()
	for event in EVENTS:
		if event.type == pygame.QUIT:
			RUNNING = False
	SCREEN.fill(BGCOLOR)

# This function calls the draw function specified by the user and does the pygame stuff neded to draw to the screen
def draw():
	if DRAWFUNC != None:
		DRAWFUNC()
	pygame.display.flip()
	CLOCK.tick(FRAMERATE)

# This function just returns the screen. Nothing more. Might remove, since it seems kinda unnecessary
def getScreen():
	return SCREEN

# This function sets the draw function to the passed function
def setDraw(function):
	global DRAWFUNC

	DRAWFUNC = function

# !! This function is only intendet to be used by ezPygame !!
# The standart function, that is executed on each frame
def standartIterationFunction():
	update()
	draw()

# This function will run a loop of the iteration function, until the window is stopped
def run():
	global RUNNING

	RUNNING = True
	while RUNNING:
		ITERATIONFUNC()

# This function stops the above described loop
def stop():
	global RUNNING

	RUNNING = False