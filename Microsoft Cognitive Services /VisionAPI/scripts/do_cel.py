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

celebrity_analyze_url = vision_base_url + "models/celebrities/analyze"
image_path ="/home/Desktop/Microsoft Cognitive Services /VisionAPI/images/Ranveer.jpg"
image_data = open(image_path, "rb").read() 
headers  = {'Ocp-Apim-Subscription-Key': subscription_key,"Content-Type":"application/octet-stream","Content-Type": "application/octet-stream"}
params   = {'model': 'celebrities'}

response = requests.post(celebrity_analyze_url, headers=headers, params=params, data=image_data)
analysis= response.json()

#print(analysis)

#assert analysis["result"]["celebrities"] is not []
celebrity_info = analysis["result"]["celebrities"][0]
celebrity_name = celebrity_info["name"]
confidence=celebrity_info["confidence"]
a=(celebrity_name, confidence)
print(a)

with open('f1','w') as f:
  f.write(celebrity_info["name"])
  f.write(",")
  f.write(str(celebrity_info["confidence"]))
  f.write(",")
