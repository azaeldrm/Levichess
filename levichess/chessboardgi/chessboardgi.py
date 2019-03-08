import pygame
import time
import os
from levichess.resources.config import config
from levichess.mainfiles.player import Player

class ChessBoardGI:
	"""description of class"""

	def main():

		# Initialize game
		pygame.init()

		# Initialize variables
		disp = pygame.display
		font = pygame.font.SysFont(None, 35)
		script_dir = config.root_path + '\\images\\'

		tile1_c = (100,50,30)
		tile2_c = (150,120,60)
		letters_c = (110,60,30)
		bg_c = (240,210,150)

		letters = ['A','B','C','D','E','F','G','H']
		piecenames = ['Rook','Knight','Bishop','King','Queen','Pawn']
		color = ['Black','White']
		board = []

		thr = 40
		hor = 300
		ver = 300
		screenSize = (hor+thr*2,ver+thr*2)
		rectSize = int((screenSize[0]-thr*2)/8)

		gameDisplay = disp.set_mode(screenSize)
		disp.set_caption('BOI ChessGame')

		d = pygame.draw
		f = gameDisplay.fill
		b = gameDisplay.blit

		# Initializing chess pieces' images
		Bpawn = pygame.image.load(os.path.join(script_dir, 'blackpawn.png'))
		Bpawn = pygame.transform.scale(Bpawn,(rectSize,rectSize))
		Brook = pygame.image.load(os.path.join(script_dir,'blackrook.png'))
		Brook = pygame.transform.scale(Brook,(rectSize,rectSize))
		Bknight = pygame.image.load(os.path.join(script_dir,'blackknight.png'))
		Bknight = pygame.transform.scale(Bknight,(rectSize,rectSize))
		Bbishop = pygame.image.load(os.path.join(script_dir,'blackbishop.png'))
		Bbishop = pygame.transform.scale(Bbishop,(rectSize,rectSize))
		Bking = pygame.image.load(os.path.join(script_dir,'blackking.png'))
		Bking = pygame.transform.scale(Bking,(rectSize,rectSize))
		Bqueen = pygame.image.load(os.path.join(script_dir,'blackqueen.png'))
		Bqueen = pygame.transform.scale(Bqueen,(rectSize,rectSize))

		Wpawn = pygame.image.load(os.path.join(script_dir,'whitepawn.png'))
		Wpawn = pygame.transform.scale(Wpawn,(rectSize,rectSize))
		Wrook = pygame.image.load(os.path.join(script_dir,'whiterook.png'))
		Wrook = pygame.transform.scale(Wrook,(rectSize,rectSize))
		Wknight = pygame.image.load(os.path.join(script_dir,'whiteknight.png'))
		Wknight = pygame.transform.scale(Wknight,(rectSize,rectSize))
		Wbishop = pygame.image.load(os.path.join(script_dir,'whitebishop.png'))
		Wbishop = pygame.transform.scale(Wbishop,(rectSize,rectSize))
		Wking = pygame.image.load(os.path.join(script_dir,'whiteking.png'))
		Wking = pygame.transform.scale(Wking,(rectSize,rectSize))
		Wqueen = pygame.image.load(os.path.join(script_dir,'whitequeen.png'))
		Wqueen = pygame.transform.scale(Wqueen,(rectSize,rectSize))

		pieceImages = [Bpawn, Brook, Bknight, Bbishop, Bking, Bqueen, Wpawn, Wrook, Wknight, Wbishop, Wking, Wqueen]

		# Generating board array
		for i in range(2):
			for j in range(6):
				board.append([color[i] + ' ' + piecenames[j]])

		# Creating functions
		def text_to_screen(msg,color,x,y):
			screen_text = font.render(msg,True,color)
			b(screen_text, [x,y])

		# === GRAPHIC ASSETS
		# Generating background
		def draw_bg():
			gameDisplay.fill(bg_c)
			for i in range(8):
				for j in range(8):
					if i%2 == 0:
						if j%2 == 0:
							f(tile2_c,rect=[thr+rectSize*i,thr+rectSize*j,rectSize,rectSize])
						elif j%2 == 1:
							f(tile1_c,rect=[thr+rectSize*i,thr+rectSize*j,rectSize,rectSize])
					elif i%2 == 1:
						if j%2 == 0:
							f(tile1_c,rect=[thr+rectSize*i,thr+rectSize*j,rectSize,rectSize])
						elif j%2 == 1:
							f(tile2_c,rect=[thr+rectSize*i,thr+rectSize*j,rectSize,rectSize])

		# Generating text
		def draw_letters():
			for i in range(8):
				for j in range(8):
					if j==0:
						text_to_screen(str(i+1), letters_c, thr-2*rectSize/3+rectSize*j, thr-3*rectSize/4+rectSize*(i+1))
					elif j==7:
						text_to_screen(str(i+1), letters_c, thr-2*rectSize/3+rectSize*(j+2), thr-3*rectSize/4+rectSize*(i+1))
			for i in range(8):
				for j in range(8):
					if i==0:
						text_to_screen(letters[j], letters_c, thr-2*rectSize/3+rectSize*(j+1), thr-3*rectSize/4+rectSize*i)
					elif i==7:
						text_to_screen(letters[j], letters_c, thr-2*rectSize/3+rectSize*(j+1), thr-3*rectSize/4+rectSize*(i+2))

		# Generating pieces
		def draw_pieces():
			board_in = config.game_board
			for i in range(len(board_in)):
				for j in range(len(board_in)):
					try:
						y, x = board_in[i][j].Location
						if board_in[i][j].colorID == 0:
							b(pieceImages[board_in[i][j].pieceID],(thr+rectSize*(x-1),thr+rectSize*(y-1)))
						elif board_in[i][j].colorID == 1:
							b(pieceImages[board_in[i][j].pieceID+6],(thr+rectSize*(x-1),thr+rectSize*(y-1)))
					except Exception as e:
						continue

		# Refreshing graphic interface
		def refreshGI():
			draw_bg()
			draw_letters()
			draw_pieces()
			disp.update()


		# Starting While loop
		refreshGI()
		config.gameExit = False
		#updateGI = False
		while config.gameExit is not True:
			# Updating game to show everything
			if config.turnSwitch is True:
				print ('UPDATING CHESSBOARD GRAPHIC INTERFACE.')
				refreshGI()
				time.sleep(1)

			# Start game loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					config.gameExit = True

		pygame.quit()
		quit()
