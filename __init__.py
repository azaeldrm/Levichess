import sys
from threading import Thread
from MainGame import MainGame
from SoundTracks.SoundTracks import SoundTracks
from ChessBoardGI.chessGI import chessGI

if __name__ == "__main__":

	SoundTracks.init_SoundTracks()
	MainGame.init_game()
	MainGame.init_boards()
	Thread(target = chessGI.main).start()
	Thread(target = MainGame.main).start()
