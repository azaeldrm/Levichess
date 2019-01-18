#!/usr/bin/env python

import sys
from threading import Thread
from MainFiles.MainGame import MainGame
from SoundTracks.SoundTracks import SoundTracks
from ChessBoardGI.ChessBoardGI import ChessBoardGI

if __name__ == "__main__":

	SoundTracks.init_SoundTracks()
	MainGame.init_game()
	MainGame.init_boards()
	Thread(target = ChessBoardGI.main).start()
	Thread(target = MainGame.main).start()
