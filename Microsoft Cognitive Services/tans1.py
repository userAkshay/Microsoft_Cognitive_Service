 #!/usr/bin/env python
# coding=utf-8
import requests
import sys
import json
import subprocess
import os

reload(sys)
sys.setdefaultencoding('utf8')


# Get access token to use the speech services
url_token_api = '************' # service address 
api_key = '********'          # Azure Cognitive API Key, replace with 


headers = {'Content-Length': '0', 'Ocp-Apim-Subscription-Key':api_key}

api_response = requests.post(url_token_api, headers=headers)

access_token = str(api_response.content.decode('utf-8'))
audio_file_path ="/home/aishwarya/Download/sample.mp3"

# Call Speech to text service
url_stt_api = 'https://speech.platform.bing.com/recognize' # service address 

headers = {'Authorization': 'Bearer {0}'.format(access_token), 
           'Content-Length': len(audio_file_path), 
           'Content-type': 'audio/wav', 
           'codec': 'audio/pcm', 
           'samplerate': '16000'}

params = urllib.parse.urlencode({
    'scenarios': 'ulm',
    'appid': 'D4D52672-91D7-4C74-8AD8-42B1D98141A5', # dont change, it is fixed by design
    'locale': 'en-US', # speech in english
    'device.os': 'PC',
    'version': '3.0',
    'format': 'json', # return value in json
    'instanceid': str(uuid.uuid1()), # any guid
    'requestid': str(uuid.uuid1()),
})

api_response = requests.post(url_stt_api, headers=headers, params=params, data=audio_file_path)
