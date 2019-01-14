from MainFiles.Piece import Piece
from MainFiles.ChessBoard import ChessBoard
from MainFiles.Cemetery import Cemetery
from Leviosa.Decoder import Decoder
from sys import exit
from enum import Enum
from SoundTracks.SoundTracks import SoundTracks
from config import config


class Player:
	"""Player class contains functions to be executed by the player in the game,
	as well as verification for Player actions which result in the validity of these."""

	def __init__(self, BlackOrWhite):
		self.BW = BlackOrWhite #Assign a Color to the Player
		self.IsPlaying = False
		self.PN = 0
		self.PName = 'Player ' + str(self.PN)
		if self.BW == 0: #Black Player
			self.ColorID = "BLACK"
		elif self.BW == 1: #White Player
			self.ColorID = "WHITE"

	def ExitGame(self):
		SoundTracks.StopSong()
		exit()

	#Function to let Player know what piece is it
	def WhatPiece(self,string): #Posts attributes of objects in black_pieces
		y, x = Decoder.NameToLocation(string)
		try:
			board = ChessBoard.board[y][x]
			try:
				if board.isValid == False:
					print('No piece in location:  ' + string)
				else:
					print(board.color + ' ' + board.piecetype + ' in location:  ' + string + '\n')
			except IndexError:
				print('Outside of boundary.'+ '\n')
		except IndexError:
			print('Outside of boundary.'+ '\n')
		return False


	def isPieceAlly(firstPiece,secondPiece):
		pieceOne = ChessBoard.getPieceFromBoard(firstPiece) #import fist Piece
		pieceTwo = ChessBoard.getPieceFromBoard(secondPiece) #Import second piece
		try:
			if pieceOne.isValid == True and pieceTwo.isValid == True:	#Check if both locations are pieces. If they are valids or not
				if (pieceOne.colorID == pieceTwo.colorID) == True:  #If their colorID match each other, they are allies
					print('Pieces are Allies. \n')					#Else, they are enemies
					return True
				else:
					print('Pieces are Enemies. \n')
					return False
			elif pieceOne.isValid == False:							#If the first locaton is not valid, there is no piece there
					print('There is no piece in location: ' + firstPiece + '\n')
					return False
		except IndexError:
			print('Outside of boundary.' + '\n')


	def isLocationClear(WhereTo): #Check for final location only
		destination = ChessBoard.getPieceFromBoard(WhereTo) #Import second piece
		try:
			if destination.isValid == False:														#Check if there is a piece in final destination
				print('There is no piece in location ' + WhereTo + '.')
				return True
			else:
				print('There is a piece in location ' + WhereTo + '.')
				return False
		except IndexError:
			print('Outside of boundary.' + '\n')


	def isPathClear(WhichPiece,WhereTo):
		pieceOne = ChessBoard.getPieceFromBoard(WhichPiece) #Decoding the Piece
		pieceTwo = ChessBoard.getPieceFromBoard(WhereTo)
		yf, xf = Decoder.NameToLocation(WhereTo)
		ys, xs = Decoder.NameToLocation(WhichPiece)
		print('Initial location: ' + str(ys) + ', ' + str(xs) + '.') #Should be yi + n (one step)
		print('Final location: ' + str(yf) + ', ' + str(xf) + '.\n') #Should be yi + n (one step)

		#Horse is the ONLY piece that is allowed to move just one. Therefore we do not need to check its path (Only final Location is suficient to check its Path)
		#If Piece is not a horse -> Check if the path is clear!
		if (pieceOne.pieceID != 2) and (pieceOne.pieceID != 0):

			if yf - ys > 0:
				ys = ys + 1
			elif yf - ys < 0:
				ys = ys - 1
			if xf - xs > 0:
				xs = xs + 1
			elif xf - xs < 0:
				xs = xs - 1

			while (abs(yf - ys) == abs(xf - xs)) or (yf > ys or yf < ys) or ((xf > xs) or (xf < xs)):
				print('Checking location ' + str(ys) + ', ' + str(xs) + '.')
				if (Piece.HowMove(pieceOne,ys,xs) == True):
					if Player.isLocationClear(Decoder.LocationToName(ys,xs)) == True:
						print('Iteration to ' + str(ys) + ',' + str(xs) + ' complete.\n')

						if yf == ys and xf == xs:
							break
						elif abs(yf - ys) == abs(xf - xs):
							if yf > ys:
								ys = ys + 1
							elif yf < ys:
								ys = ys - 1
							if xf > xs:
								xs = xs + 1
							elif xf < xs:
								xs = xs - 1
							continue
						if yf > ys:
							ys = ys + 1
							continue
						elif yf < ys:
							ys = ys - 1
							continue
						elif xf > xs:
							xs = xs + 1
							continue
						elif xf < xs:
							xs = xs - 1
							continue

					else:
						print('Stopped here: ' + str(ys) + ',' + str(xs))
						break
				else:
					ys = ys + 1
					print('Iteration to ' + str(ys) + ',' + str(xs) + ' complete.')
					break
		#If Piece is a Horse, do not need to check this equation -> Pass
		else:
			ys = yf
			xs = xf
			pass

		print ('Returned: ' + str(ys) + ',' + str(xs) + '\n')
		return ys, xs


	def isMoveValid(WhichPiece,WhereTo):
		yf, xf = Decoder.NameToLocation(WhereTo) #Decoding the desired location
		pieceOne = ChessBoard.getPieceFromBoard(WhichPiece) #import fist Piece
		pieceTwo = ChessBoard.getPieceFromBoard(WhereTo) #Import second piece
		try:
			##Check if the move is valid (check moveRules)
			if (pieceOne.HowMove(yf,xf) == True) or (pieceOne.HowKill(yf,xf) == True):
				print(str(pieceOne.HowMove(yf,xf)) + ' Move')
				print(str(pieceOne.HowKill(yf,xf)) + ' Kill')
				#Check if Location is Clear
				#If Location is Clear:
				if Player.isLocationClear(WhereTo) == True:
					if (pieceOne.pieceID !=0)  or ((pieceOne.pieceID == 0) and pieceOne.HowKill(yf,xf) == False):
						#Proceed to check if there is a piece blocking the move
						ys, xs = Player.isPathClear(WhichPiece,WhereTo)			#Runs a loop checking each x and y, and return the last one. If the last is equal to the desired location, it can move there.
						#If the path is clear (no piece on its way)
						if yf == ys and xf == xs:
							print('Yes, ' + pieceOne.color + ' ' + pieceOne.piecetype + ' can move from ' + WhichPiece + ' to ' + WhereTo + ' because the Path is clear.')
							return True, False
						#If there is a piece on it's way you cannot move
						else:
							print('No, ' + pieceOne.color + ' ' + pieceOne.piecetype + ' cannot move from ' + WhichPiece + ' to ' + WhereTo + ' because there is a piece in the way. ' + '[Other Piece at Location: ' + Decoder.LocationToName(ys,xs) + ']\n')
							return False, False
					else:
						print('No, ' + pieceOne.color + ' ' + pieceOne.piecetype + ' cannot move from ' + WhichPiece + ' to ' + WhereTo + ' because it is a Pawn, and cannot move diagonally.\n')
						return False, False

				#If Location is not Clear:
				#Check if Piece is an Ally
				elif Player.isPieceAlly(WhichPiece,WhereTo) == False: #Other piece is enemy -> KILL
					ys, xs = Player.isPathClear(WhichPiece,WhereTo)
					#If the path is clear (no piece on its way):
					if yf == ys and xf == xs:
						#Check if the piece can kill (if killType is Valid):

						if pieceOne.HowKill(yf,xf) == True:
							#If the KillType is valid -> Can Kill
							print('Yes, ' + pieceOne.color + ' ' + pieceOne.piecetype + ' can move from ' + WhichPiece + ' to ' + WhereTo + ' and kill ' + pieceTwo.color + ' ' + pieceTwo.piecetype + '.\n')
							return True, True
						else:
							#If the KillType is NOT valid -> Cannot move there
							print('No, ' + pieceOne.color + ' ' + pieceOne.piecetype + ' cannot move from ' + WhichPiece + ' to ' + WhereTo + ' because there it is not a valid Kill Type.\n')
							return False, False
					#If there is a piece on it's way you cannot move
					else:
						print('No, ' + pieceOne.color + ' ' + pieceOne.piecetype + ' cannot move from ' + WhichPiece + ' to ' + WhereTo + ' because there is a piece in the way. ' + '[Other Piece at Location: ' + Decoder.LocationToName(ys,xs) + ']\n')
						return False, False
					#If the Piece is an Ally, it cannot kill or move there
				else:
					print('No, ' +  pieceOne.color + ' ' + pieceOne.piecetype + ' cannot move from ' + WhichPiece + ' to ' + WhereTo + ' because there is an ally piece at this location.\n')
					return False, False
			#If the move is Invalid, it cannot proceed
			else:
				print('No, ' +  pieceOne.color + ' ' + pieceOne.piecetype + ' cannot move from ' + WhichPiece + ' to ' + WhereTo + ' because it is an invalid move.\n')
				return False, False
		except IndexError:
			print('Outside of boundary.')

	def KillPiece(pieceOne): #Function will be used to move motors to the cemetery
		Cemetery.MovePieceToCemetery(pieceOne)


	def MovePiece(self,WhichPiece,WhereTo): #Take Both String Locations. Like A2 or B7
		pieceOne = ChessBoard.getPieceFromBoard(WhichPiece) #import fist Piece
		pieceTwo = ChessBoard.getPieceFromBoard(WhereTo) #Import second piece
		try:
			if self.BW == pieceOne.colorID:
				MoveValidation,KillValidation = Player.isMoveValid(WhichPiece,WhereTo)
				if (MoveValidation == True) and (KillValidation == False): #Just Move The Piece
					ChessBoard.MovePieceInBoard(pieceOne,WhereTo)
					SoundTracks.PlaySound(SoundTracks.Woosh1)
					print('Player ' + str(self.PN) + ' moves ' + pieceOne.color + ' ' + pieceOne.piecetype + ' from ' + WhichPiece + ' to ' + WhereTo + '.\n')
					return True
				elif (MoveValidation == True) and (KillValidation == True):
					Player.KillPiece(pieceTwo)
					ChessBoard.MovePieceInBoard(pieceOne,WhereTo)
					SoundTracks.PlaySound(SoundTracks.Woosh1)
					print('Player ' + str(self.PN) + ' moves ' + pieceOne.color + ' ' + pieceOne.piecetype + ' from ' + WhichPiece + ' to ' + WhereTo + ' and kills ' + pieceTwo.piecetype + '.\n')
					return True
				else:
					print(pieceOne.color + ' ' + pieceOne.piecetype + ' move aborted.\n')
					print('Try again.\n')
					return False
			else:
				print('This is not a Piece from your team. Please, try again.\n')
				return False
		except IndexError:
			print('Outside of boundary.' + '\n')
			return False

	def SeeCemetery(self):
		Cemetery.printCemetery(Cemetery.cboard)


	def GodMovePiece(self,WhichPiece,WhereTo):
		yf, xf = Decoder.NameToLocation(WhereTo) #Decoding the desired location
		ThisPiece = ChessBoard.getPieceFromBoard(WhichPiece) #Decoding the Piece
		try:
			if ThisPiece.isValid == True:
				y, x = ThisPiece.Location
				Cemetery.MovePieceToCemetery(ThisPiece)
				config.game_board[y][x] = ChessBoard.Blank
			elif ThisPiece.isValid == False:
				pass
			ChessBoard.MovePieceInBoard(ThisPiece,WhereTo)
			SoundTracks.PlaySound(SoundTracks.Woosh1)
			print('Teleporting ' + ThisPiece.color + ' ' + ThisPiece.piecetype + ' from ' + WhichPiece + ' to ' + WhereTo + '.\n')
			return True
		except IndexError:
			print('Outside of boundary.' + '\n')

#	def GodOfWar(self,WhichPiece):
#		ThisPiece = ChessBoard.getPieceFromBoard(WhichPiece) #Decoding the Piece
#		if ThisPiece.isValid == True:
#			y, x = ThisPiece.Location
#			Cemetery.MovePieceToCemetery(ThisPiece)
#			config.game_board[y][x] = ChessBoard.Blank
#		else:
#			print('BlankSpaces are ancient legends. They came before everything and occupy every empty space. \nEven Gods do not have the power to kill a BlankSpace...\n')
