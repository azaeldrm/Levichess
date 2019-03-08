from google.cloud import speech
import io
import os
from levichess.leviosa import position_generator as gen
from levichess.resources.config import config

def googleMain():
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "levichess/resources/keys/levichess_key.json"
	speech_file = 'file.flac'
	sentence = ''
	syntax = config.syntaxArray

	with io.open(speech_file, 'rb') as audio_file:
	        content = audio_file.read()

	client = speech.SpeechClient()
	response = client.recognize(
	    audio=speech.types.RecognitionAudio(
	        content=content,
	    ),
	    config=speech.types.RecognitionConfig(
	        encoding='FLAC',
	        language_code='en-US',
	        sample_rate_hertz=16000,
	        speech_contexts=[speech.types.SpeechContext(
	            phrases=syntax,
	        )],
	    )
	)

	for result in response.results:
		#print('=' * 20)
		sentence = sentence + result.alternatives[0].transcript

	#print('=' * 20)
	#print('Transcript: ' + sentence)
	#print('Confidence: ' + str(result.alternatives[0].confidence))
	#print('=' * 20)

	return sentence
