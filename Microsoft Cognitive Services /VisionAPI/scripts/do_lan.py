 #!/usr/bin/env python
# coding=utf-8
import requests
import sys 
import json 
import subprocess
import os 
reload(sys)
sys.setdefaultencoding('utf8')

subscription_key = '***********'
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
landmark_analyze_url = vision_base_url + "models/landmarks/analyze"

headers  = {'Ocp-Apim-Subscription-Key': subscription_key,"Content-Type": "application/octet-stream"}
params   = {'model': 'landmarks'}

image_path ="/home/Desktop/Microsoft Cognitive Services /VisionAPI/images/bluemasjid.jpg"
image_data = open(image_path, "rb").read() 


response = requests.post(landmark_analyze_url, headers=headers, params=params, data=image_data)

analysis= response.json()

print (analysis)
assert analysis["result"]["landmarks"] is not []
landmark_name = analysis["result"]["landmarks"][0]["name"].capitalize()
confidence = analysis["result"]["landmarks"][0]["confidence"]












