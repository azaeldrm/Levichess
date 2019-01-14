from PieceTypes.Blank import Blank
from PieceTypes.Bishop import Bishop
from PieceTypes.King import King
from PieceTypes.Knight import Knight
from PieceTypes.Pawn import Pawn
from PieceTypes.Queen import Queen
from PieceTypes.Rook import Rook
from Leviosa.Decoder import Decoder
from MainFiles.Piece import Piece
from config import config


class ChessBoard:
	def __init__(self):
		pass

	# Blank object created to be repeated throughout board. Reference to only one pointer
	pBlank = Blank()

	def init_board(board_in):
		for i in range(10):
			board_in.append(['.']*10)

	def start_board(board_in): #start board initializes the function init_board automatic. It take as argument a board
		ChessBoard.init_board(board_in)
		for i in range(10):
			for j in range(10):
				if j == 0 or j == 9:
					board_in[i][j] = ChessBoard.pBlank
				if i==0 or i == 9:
					board_in[i][j] = ChessBoard.pBlank
				elif i==1:
					if j==1:
						board_in[i][j] = Rook(0,1)
						board_in[i][abs(j-len(range(9)))] = Rook(0,2)
						board_in[i][j].Location = [i,j]
						board_in[i][abs(j-len(range(9)))].Location = [i,abs(j-len(range(9)))]
					elif j==2:
						board_in[i][j] = Knight(0,1)
						board_in[i][abs(j-len(range(9)))] = Knight(0,2)
						board_in[i][j].Location = [i,j]
						board_in[i][abs(j-len(range(9)))].Location = [i,abs(j-len(range(9)))]
					elif j==3:
						board_in[i][j] = Bishop(0,1)
						board_in[i][abs(j-len(range(9)))] = Bishop(0,2)
						board_in[i][j].Location = [i,j]
						board_in[i][abs(j-len(range(9)))].Location = [i,abs(j-len(range(9)))]
					elif j==4:
						board_in[i][j] = Queen(0,1)
						board_in[i][j].Location = [i,j]
					elif j==5:
						board_in[i][j] = King(0,1)
						board_in[i][j].Location = [i,j]
				elif (i==2 and j!=0) and (i==2 and j!=9):
					board_in[i][j] = Pawn(0,j)
					board_in[i][j].Location = [i,j]
				elif i>=3 and i<=6:
					board_in[i][j] = ChessBoard.pBlank
				elif (i==7 and j!=0) and (i==7 and j!=9):
					board_in[i][j] = Pawn(1,j)
					board_in[i][j].Location = [i,j]
				elif i==8:
					if j==1:
						board_in[i][j] = Rook(1,1)
						board_in[i][abs(j-len(range(9)))] = Rook(1,2)
						board_in[i][j].Location = [i,j]
						board_in[i][abs(j-len(range(9)))].Location = [i,abs(j-len(range(9)))]
					elif j==2:
						board_in[i][j] = Knight(1,1)
						board_in[i][abs(j-len(range(9)))] = Knight(1,2)
						board_in[i][j].Location = [i,j]
						board_in[i][abs(j-len(range(9)))].Location = [i,abs(j-len(range(9)))]
					elif j==3:
						board_in[i][j] = Bishop(1,1)
						board_in[i][abs(j-len(range(9)))] = Bishop(1,2)
						board_in[i][j].Location = [i,j]
						board_in[i][abs(j-len(range(9)))].Location = [i,abs(j-len(range(9)))]
					elif j==4:
						board_in[i][j] = Queen(1,1)
						board_in[i][j].Location = [i,j]
					elif j==5:
						board_in[i][j] = King(1,1)
						board_in[i][j].Location = [i,j]
		return board_in

	def print_board(board_in,trigger=1):
		board_out = []
		BlankSpace = '             '
		Letter = ('BOISEChess','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'BOISEChess')
		Number = ('','1', '2', '3', '4', '5', '6', '7', '8', '')

		print('_.'*90+'_\n')
		for i in range(len(board_in)):
			board_out.append(['.']*10)
			for j in range(len(board_in)):
				if board_in[i][j].isValid == True:
					if trigger == 1:
						board_out[i][j] = board_in[i][j].color + ' ' + board_in[i][j].piecetype + ' '*(len(BlankSpace)-len(board_in[i][j].piecetype)-len(board_in[i][j].color))
					elif trigger != 1:
						board_out[i][j] = board_in[i][j]
				elif board_in[i][j].isValid == False:
					if i == 0:
						board_out[i][j] = Letter[j] + ' '*(len(BlankSpace)-len(Letter[j])+1)
					elif i > 0 and j == 0:
						board_out[i][j] = Number[i] + ' '*(len(BlankSpace)-len(Number[i])+1)
					elif i > 0 and j == 9:
						board_out[i][j] = Number[i] + ' '*(len(BlankSpace)-len(Number[i])+1)
					elif i > 0 and j != 0:
						board_out[i][j] = BlankSpace + ' '
					if i == 9:
						board_out[i][j] = Letter[j] + ' '*(len(BlankSpace)-len(Letter[j])+1)
			print (board_out[i])
		print('_.'*90+'_\n\n')

	#Function that, instead of writing board[][] everytime, you can write A3 and returns the piece of that location
	def getPieceFromBoard(string):
		y, x = Decoder.NameToLocation(string)
		return config.game_board[y][x]

	# Verification as to whether config.game_board has been initialized might need to be added
	def MovePieceInBoard(ThisPiece,WhereTo):
		yi, xi = ThisPiece.Location
		yf, xf = Decoder.NameToLocation(WhereTo)
		board = config.game_board
		board[yf][xf] = ThisPiece
		board[yf][xf].Location = [yf, xf]
		board[yi][xi] = ChessBoard.pBlank

	def CheckIfLocationIsPiece(y,x):
		if config.game_board[y][x].valid == True:
			print('Piece')
			return True
		else:
			print('Blank')
			return False
