class config:
	"""
	config contains variables that, if imported by a Class, can be used and
	modified by this class and changes will reflect in all other Classes that
	have imported config.
	"""
	import os

	gameExit = False
	turnSwitch = False
	syntaxArray = []
	game_board = []
	game_cboard = []
	root_path = os.path.dirname(__file__)
