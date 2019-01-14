import pyaudio
import wave
import subprocess
from Leviosa import Interpreter_GoogleAPI as gAPI

class Listener:

	def listen(seconds):
		FORMAT = pyaudio.paInt16
		CHANNELS = 1
		RATE = 44100
		CHUNK = 1024
		RECORD_SECONDS = seconds
		WAVE_OUTPUT_FILENAME = "file.wav"

		audio = pyaudio.PyAudio()

		# start Recording
		stream = audio.open(format=FORMAT, channels=CHANNELS,
						rate=RATE, input=True,
						frames_per_buffer=CHUNK)
		print ("Speak.",end='\n')
		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
		print("Done listening!\n")

		# stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()

		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()


		command = 'sox file.wav --rate 16000 --bits 16 --endian little --channels 1 file.flac'
		flag_done = subprocess.call(command, shell=True)

		sentence = gAPI.googleMain()
		return sentence
