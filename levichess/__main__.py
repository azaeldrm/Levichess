#!/usr/bin/env python

import sys
from threading import Thread
from levichess.mainfiles.maingame import MainGame
from levichess.soundtracks.soundtracks import SoundTracks
from levichess.chessboardgi.chessboardgi import ChessBoardGI

if __name__ == "__main__":

	SoundTracks.init_SoundTracks()
	MainGame.init_game()
	MainGame.init_boards()
	Thread(target = ChessBoardGI.main).start()
	Thread(target = MainGame.main).start()
