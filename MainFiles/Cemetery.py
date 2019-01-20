from PieceTypes.Blank import Blank
from MainFiles.ChessBoard import ChessBoard
from MainFiles.Piece import Piece
from config import config


class Cemetery:
	"""description of class"""
	def __init__(self):
		pass

	# Blank object created to be repeated throughout board. Reference to only one pointer
	cBlank = Blank()

	def init_board(board_in):
		for i in range(2):
			board_in.append(['.']*16)

	def start_board(board_in):
		Cemetery.init_board(board_in)
		for i in range(2):
			for j in range(16):
				board_in[i][j] = Cemetery.cBlank
		return board_in

	def printCemetery(board_in,trigger=1):
		board_out = []
		Teams = ['BlackPanthers Team', 'Gandalfs Team     ']
		BlankSpace = '     '
		print('Cemetery: \n')
		for i in range(2):
			board_out.append(['.']*16)
			for j in range(16):
				if (i==0) and (j==0):
					board_out[i][j] = Teams[i] + ' '*(len(BlankSpace)-len(Teams[j])+1)
				elif (i==1) and (j==0):
					board_out[i][j] = Teams[i] + ' '*(len(BlankSpace)-len(Teams[j])+1)
				elif board_in[i][j].isValid == True:
					if trigger == 1:
						board_out[i][j] = board_in[i][j].color + ' ' + board_in[i][j].piecetype + ' '*(len(BlankSpace)-len(board_in[i][j].piecetype)-len(board_in[i][j].color))
					elif trigger != 1:
						board_out[i][j] = board_in[i][j]
				elif board_in[i][j].isValid == False:
					board_out[i][j] = BlankSpace + ' '
			print (board_out[i])
		print('\n')

	def CheckEmptyLocation(WhichTeam,WhichLocation):
		Where = config.game_cboard[WhichTeam][WhichLocation]
		if Where.isValid == True: #Check if there is a piece in the especific location
			return False	#If there is a Piece, then the plase if ocupied. Therefore return False
		elif Where.isValid == False:
			return True		#If there is no piece, then the place is empty and can be ocupied. Return True


	def MovePieceToCemetery(DeadPiece=Piece):
		yi, xi = DeadPiece.Location
		DeadPiece.isAlive = False
		DeadPiece.Location = [False, False]
		WhichTeam = DeadPiece.colorID
		cboard = config.game_cboard
		if (DeadPiece.pieceID == 0):
			WhichLocation = 1
			while WhichLocation < 9:
				if Cemetery.CheckEmptyLocation(WhichTeam,WhichLocation) == True:
					cboard[WhichTeam][WhichLocation] = DeadPiece
					break
				else:
					WhichLocation = WhichLocation + 1
		elif (DeadPiece.pieceID == 1):
			WhichLocation = 9
			while WhichLocation < 11:
				if Cemetery.CheckEmptyLocation(WhichTeam,WhichLocation) == True:
					cboard[WhichTeam][WhichLocation] = DeadPiece
					break
				else:
					WhichLocation = WhichLocation + 1
		elif (DeadPiece.pieceID == 2):
			WhichLocation = 11
			while WhichLocation < 13:
				if Cemetery.CheckEmptyLocation(WhichTeam,WhichLocation) == True:
					cboard[WhichTeam][WhichLocation] = DeadPiece
					break
				else:
					WhichLocation = WhichLocation + 1
		elif (DeadPiece.pieceID == 3):
			WhichLocation = 13
			while WhichLocation < 15:
				if Cemetery.CheckEmptyLocation(WhichTeam,WhichLocation) == True:
					cboard[WhichTeam][WhichLocation] = DeadPiece
					break
				else:
					WhichLocation = WhichLocation + 1
		elif (DeadPiece.pieceID == 5):
			WhichLocation = 15
			if Cemetery.CheckEmptyLocation(WhichTeam,WhichLocation) == True:
					cboard[WhichTeam][WhichLocation] = DeadPiece
			else:
				print('Error, your Queen is Already Dead')
		Cemetery.printCemetery(cboard)
