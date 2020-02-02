import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

client = speech.SpeechClient.from_service_account_json('cred.json')

with io.open('bad.flac','rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz = 16000,
    language_code='en-US')

response = client.recognize(config, audio)

for result in response.results:
    print('Text: ()'.format(result.alternatives[0].transcript))


