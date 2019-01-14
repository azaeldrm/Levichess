from time import sleep
from MainFiles.ChessBoard import ChessBoard
from MainFiles.Piece import Piece
from MainFiles.Player import Player
from MainFiles.Cemetery import Cemetery
from SoundTracks.SoundTracks import SoundTracks
from Leviosa.Listener import Listener
from config import config
from Leviosa import PositionGenerator as gen


class MainGame:

	def init_players(choice):

		global Player1, Player2

		Player.IsPlaying = True
		WhitePlayer = Player(1)
		BlackPlayer = Player(0)

		if choice == True:
			Player1, Player2 = WhitePlayer, BlackPlayer
			print('\nPlayer 1 assigned White pieces!\n')
		elif choice == False:
			Player1, Player2 = BlackPlayer, WhitePlayer
			print('\nPlayer 1 assigned Black pieces!\n')

		Player1.PN = 1
		Player2.PN = 2


	def init_game():

		# Dialogue
		print('\n'*60)
		print('LEVICHESS\n')
		print('Version 1')
		print('='*200+'\n\n')
		sleep(0.7)
		print('Prepare yourself! Wingardium Leviosa!\n')
		sleep(0.7)
		print('...\n')
		sleep(0.7)
		# print('Before we start, CHOOSE YOUR LEGION!\n\nWould you control BLACK or WHITE pieces?')

		while True:
			# choice = input().lower()
			choice = 'white'
			if choice == 'white':
				MainGame.init_players(True)
				break
			elif choice == 'black':
				MainGame.init_players(False)
				break
			else:
				print('\nPlease, choose a valid color.')

		SoundTracks.PlayThemeSong(SoundTracks.HarryPotter_Theme)

		print('Gathering troops...\n')
		print('...')
		sleep(0.7)
		print('\nTroops are ready.\nJoining the Battle.\n')
		print('...')
		sleep(0.7)

		print('\nGood Luck, Wizard. You\' need it!')
		sleep(1.5)
		print('\n'*60)



	def init_boards():
		ChessBoard.start_board(config.game_board)
		Cemetery.start_board(config.game_cboard)


	def main():

		global Player1, Player2
		if Player1.BW == 1:
			PlayerTurn = [Player1, Player2]
		elif Player1.BW == 0:
			PlayerTurn = [Player2, Player1]

		locationArray = ['A1','B1','C1','D1','E1','F1','G1','H1',
				   'A2','B2','C2','D2','E2','F2','G2','H2',
				   'A3','B3','C3','D3','E3','F3','G3','H3',
				   'A4','B4','C4','D4','E4','F4','G4','H4',
				   'A5','B5','C5','D5','E5','F5','G5','H5',
				   'A6','B6','C6','D6','E6','F6','G6','H6',
				   'A7','B7','C7','D7','E7','F7','G7','H7',
				   'A8','B8','C8','D8','E8','F8','G8','H8']
		DURATION = 4

		config.syntaxArray = gen.syntax()

		while config.gameExit is not True:
			try:
				for i in range(2):
					config.turnSwitch = False
					while config.turnSwitch == False:
						moveArray = []
						sentenceArray = []
						print('Player ' + str(PlayerTurn[i].PN) + ' ( ' + str(PlayerTurn[i].ColorID) + ' )' + ' turn.\n')
						# Commented out print function because we already have a graphic interface
						#ChessBoard.print_board(config.game_board)
						print('What is the next move, Wizard?')
						sentence = Listener.listen(DURATION)
						print('\n'*60)

						if (sentence is not '') and ('exit' not in sentence): # No.1
							sentenceArray = sentence.split(' ')
							for j in range(len(sentenceArray)):
								if sentenceArray[j].upper() in locationArray:
									if sentenceArray[j].upper() not in moveArray[:]:
										moveArray.append(sentenceArray[j].upper())

							# This prints the sentence recorded and the chessboard locations extracted from it.
							print(sentenceArray)
							print(moveArray)

							# This executes the commands if two chessboard locations were extracted.
							if len(moveArray) == 2 and 'teleport' not in sentence:
								config.turnSwitch = PlayerTurn[i].MovePiece(moveArray[0],moveArray[1])
								if config.turnSwitch == True:
									print('Loop is True. Next turn!\n')
									#config.turnSwitch = True #This is not needed anymore, as config.turnSwitch returns a boolean.
								else:
									print('Loop is ' + str(config.turnSwitch) + '. Same turn.\n')
									config.turnSwitch = False
							elif len(moveArray) == 2 and 'teleport' in sentence:
								config.turnSwitch = PlayerTurn[i].GodMovePiece(moveArray[0],moveArray[1])
								print('Loop is True. Next turn!\n')
								#config.turnSwitch = True #This is not needed anymore, as config.turnSwitch returns a boolean.


						elif 'exit' in sentence: # No. 2
							print('Would you like to close the game?')
							while True:
								sentence = listen(DURATION/2)
								if 'yes' in sentence:
									config.gameExit = True
									PlayerTurn[i].ExitGame()
								elif 'no' in sentence:
									print('\n'*80)
									break
								else:
									pass

			except Exception as e:
				print('Error: ' + str(e) + '. \nTry again. \n(Same turn) \n')

			except SystemExit:
				print('Press Enter to exit.')
				quit()
