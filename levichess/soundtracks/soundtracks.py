import pygame
import os
import sys
from levichess.resources.config import config


class SoundTracks:

	script_dir = config.root_path

	#Loading the path of musics
	HarryPotter_Theme = os.path.join(script_dir, 'music\\HarryPotterThemeSong.mp3')
	EpicScore_PrepareForTheOnslaught = os.path.join(script_dir, 'music\\OrchestralChoirBattle.mp3')

	#Loading the path of Sounds
	Woosh1 = os.path.join(script_dir, 'sounds\\whoosh1.wav')


	def init_SoundTracks():
		pygame.mixer.init()

	def PlaySong(WhichSong):
		pygame.mixer.music.load(WhichSong)
		pygame.mixer.music.play()

	def PlayThemeSong(WhichTheme):
		pygame.mixer.music.load(WhichTheme)
		pygame.mixer.music.set_volume(0.7)
		pygame.mixer.music.play(loops=-1)

	def PlaySound(WhichSound):
		Sound = pygame.mixer.Sound(WhichSound)
		Sound.play()

	def StopSong():
		pygame.mixer.music.stop()
