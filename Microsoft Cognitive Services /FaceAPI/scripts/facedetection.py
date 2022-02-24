 #!/usr/bin/env python
# coding=utf-8
import requests
import sys
import json
import subprocess
import os

reload(sys)
sys.setdefaultencoding('utf8')

subscription_key = "******"
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

image_path ="/home/Desktop/Microsoft Cognitive Services /FaceAPI/BD.jpg"
image_data = open(image_path, "rb").read()

headers = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream"}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}
response = requests.post(
    face_api_url, params=params, headers=headers,data=image_data,proxies=proxies)
analysis = response.json()





f=open("f1", "w")
for line in analysis:
   gender=line["faceAttributes"]["gender"].capitalize()
   f.write(str(gender))
   f.write(",")
   age=line["faceAttributes"]["age"]
   f.write(str(age))
   f.write(",")
   smile=line["faceAttributes"]["smile"]
   if smile > 0.5:
      smile="Smiling"
   elif smile < 0.5:
      smile = "No Smile"
   elif smile : "Semi-Smile" 
   f.write(str(smile))
   f.write(",")
   glasses=line["faceAttributes"]["glasses"]
   f.write(str(glasses))
   f.write(",")
   sadness=line["faceAttributes"]["emotion"]["sadness"]
   if sadness >= 0.4:
      sadness='Sad'
   elif sadness < 0.4:
      sadness='Not-sad'
   f.write(str(sadness))
   f.write(",")
   happiness=line["faceAttributes"]["emotion"]["happiness"]
   if happiness >= 0.5:
      happiness='Yes'
   elif happiness < 0.5:
      happiness='No'
   f.write(str(happiness))
   f.write(",")
   disgust=line["faceAttributes"]["emotion"]["disgust"]
   if disgust >= 0.5:
      disgust='Yes'
   elif disgust < 0.5:
      disgust='No'
   f.write(str(disgust))
   f.write(",")
   anger=line["faceAttributes"]["emotion"]["anger"]
   if anger >= 0.5:
      anger='Yes'
   elif anger < 0.5:
      anger='No'
   f.write(str(anger))
   f.write(",")
   surprise=line["faceAttributes"]["emotion"]["surprise"]
   if surprise >= 0.5:
      surprise='Yes'
   elif surprise < 0.5:
      surprise='No'
   f.write(str(surprise))
   f.write(",")
   fear=line["faceAttributes"]["emotion"]["fear"]
   if fear >= 0.5:
      fear='Yes'
   elif fear < 0.5:
      fear='No'
   f.write(str(fear))
   f.write(",")
   lipmakeup=line["faceAttributes"]["makeup"]["lipMakeup"]
   if lipmakeup >= 0.5:
      lipmakeup ='Yes'
   elif lipmakeup < 0.5:
      lipmakeup='No'
   f.write(str(lipmakeup))
   f.write(",")
   eyeMakeup=line["faceAttributes"]["makeup"]["eyeMakeup"]
   if eyeMakeup >= 0.5:
      eyeMakeup ='Yes'
   elif eyeMakeup < 0.5:
      eyeMakeup='No'
   f.write(str(eyeMakeup))
   f.write(",")
   hairbald=line["faceAttributes"]["hair"]["bald"]
   if hairbald > 0.5:
      hairbald='Yes'
   elif hairbald < 0.5:
      hairbald= 'No'
   elif hairbald :'half-bald'
   f.write(str(hairbald))
   f.write(",")
   moustache=line["faceAttributes"]["facialHair"]["moustache"]
   if moustache >= 0.4:
      moustache='Yes'
   elif moustache < 0.4:
      moustache= 'No'
   f.write(str(moustache))
   f.write(",")
   beard=line["faceAttributes"]["facialHair"]["beard"]
   if beard >= 0.4:
      beard='Yes'
   elif beard < 0.4:
      beard= False
   elif beard :'No'
   f.write(str(beard))
   f.write("\n")

  
f.close()

