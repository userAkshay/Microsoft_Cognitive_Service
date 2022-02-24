#!/usr/bin/env python
# coding=utf-8
import requests
import sys 
import json 
import subprocess
import os 
reload(sys)
sys.setdefaultencoding('utf8')

  
subscription_key = '**********'
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
ocr_url = vision_base_url + "ocr"

headers  = {'Ocp-Apim-Subscription-Key': subscription_key,"Content-Type": "application/octet-stream"}
params   = {'language': 'unk', 'detectOrientation ': 'true'}

image_path ="/home/Desktop/Microsoft Cognitive Services /VisionAPI/images/ocr2.jpg"
image_data = open(image_path, "rb").read() 



response = requests.post(ocr_url, headers=headers, params=params, data=image_data)

analysis = response.json()

#print(analysis)

line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)


result = ""
for bla in word_infos:
   resul += bla["text"] + " "

print(result)




