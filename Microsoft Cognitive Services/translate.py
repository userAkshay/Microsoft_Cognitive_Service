import requests
import sys
import json
import subprocess
import os
from scipy.io import wavfile



reload(sys)
sys.setdefaultencoding('utf8')

subscription_key = "**************"
assert subscription_key

spe_url = "https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=en-us&format=detailed"



fs, audio_data = wavfile.read("/home/aishwarya/Downloads/sample.wav")


#print(audio_data)


headers  = {'Accept': 'application/json;text/xml', "Content-Type": "audio/wav; codec=audio/pcm; samplerate=16000",'Ocp-Apim-Subscription-Key': subscription_key,'Host':'speech.platform.bing.com','Expect':'100-continue'}



response = requests.post(spe_url, headers=headers,data=audio_data)

analysis = response.json()

