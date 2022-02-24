 #!/usr/bin/env python
# coding=utf-8
import requests
import sys
import json
import subprocess
import os

reload(sys)
sys.setdefaultencoding('utf8')




subscription_key = '*************'
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

vision_analyze_url = vision_base_url + "analyze"


image_path ="/home/Desktop/Microsoft Cognitive Services /VisionAPI/images/chitta.jpg"
image_data = open(image_path, "rb").read()


headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }
params   = {'visualFeatures': 'Categories,Description,Color'}

response = requests.post(vision_analyze_url, headers=headers, params=params, data=image_data)

analysis = response.json()

#backgroound color [dictionary]
background_color=analysis["color"]["dominantColors"]
color = ""
for idx in background_color:
    color += idx+" "

#image tag [dictionary]
tags=analysis["description"]["tags"]
keytags=""
for idx in tags:
    keytags+= idx+" "

image_caption = analysis["description"]["captions"][0]["text"].capitalize()
confidence = analysis["description"]["captions"][0]["confidence"]
name=analysis["categories"][0]["name"]
print(color)
print(name)
print(image_caption)
print(confidence)
print(keytags)



