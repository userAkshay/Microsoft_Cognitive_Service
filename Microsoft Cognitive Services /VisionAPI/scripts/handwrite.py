#!/usr/bin/env python
# coding=utf-8
import requests
import sys 
import subprocess
import json 
import time
import os

reload(sys)
sys.setdefaultencoding('utf8')

subscription_key = '********'
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
text_recognition_url = vision_base_url + "RecognizeText"


headers  = {'Ocp-Apim-Subscription-Key': subscription_key,"Content-Type": "application/octet-stream"}
params   = {'handwriting' : True}
image_path ="/home/Desktop/Microsoft Cognitive Services /VisionAPI/images/h2.jpg"
image_data = open(image_path, "rb").read()


response = requests.post(text_recognition_url, headers=headers, params=params,data=image_data)


analysis = {}


while not "recognitionResult" in analysis:
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    analysis = response_final.json()
    time.sleep(1)

text = [(line["text"]) for line in analysis["recognitionResult"]["lines"]]

#print(text.get["text"])

value = ""
for idx in text:
    value += idx+"\n"
print(value)




