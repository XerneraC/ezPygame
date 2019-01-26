try:
	import pygame
except ModuleNotFoundError:
	raise ModuleNotFoundError("Could not locate pygame")

# All the variables, ezPygame needs.
CLOCK = None
SCREEN = None
FRAMERATE = None
RUNNING = False
EVENTS = []
BGCOLOR = None
DRAWFUNC = None
ITERATIONFUNC = __stdItFunc__


def init(windowSize, bgColor = (0, 0, 0), framerate = 60):
	"""Initialize ezPygame"""

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
	ITERATIONFUNC = __stdItFunc__


def update():
	"""Do task, that need to be performed on every frame."""
	global EVENTS
	global RUNNING

	EVENTS = pygame.event.get()
	for event in EVENTS:
		if event.type == pygame.QUIT:
			RUNNING = False
	SCREEN.fill(BGCOLOR)


def draw():
	"""Call the draw function specified and update the screen."""
	if DRAWFUNC != None:
		DRAWFUNC()
	pygame.display.flip()
	CLOCK.tick(FRAMERATE)


def getScreen():
	"""
	Return the screen's surface.
	Nothing more.
	I might remove this function, since it seems kinda unnecessary, because 'ezPygame.SCREEN' is alot easier.
	"""
	return SCREEN


def setDraw(function):
	"""
	Set the draw function to the passed function.
	The draw function passed will be called every frame, and is intendet to house all the drawing code.
	It can also be used to do other stuff, that has to be done on every frame, like handling inputs.
	"""
	global DRAWFUNC

	DRAWFUNC = function


def __stdItFunc__():
	"""
	!!  This function is only intendet to be used inside of ezPygame  !!
	It's the standart function that gets called every frame, that calls update and draw.
	If you want to change this function, you can set ezPygame.ITERATIONFUNC to a function, that you have declared yourself.
	"""
	update()
	draw()


def run():
	"""Runs the infinite loop, that calls the iteration function on every frame."""
	global RUNNING

	RUNNING = True
	while RUNNING:
		ITERATIONFUNC()


def stop():
	"""Stops the infinite loop."""
	global RUNNING

	RUNNING = False