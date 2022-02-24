#!/usr/bin/env python
# coding=utf-8
import requests
import sys 
import json 
reload(sys)
sys.setdefaultencoding('utf8')


print(sys.argv[0])
print(sys.argv[1])

subscription_key = '************'
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)
Documents=json.load(open(sys.argv[1]))

#print(Documents)

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=Documents)
key_phrases = response.json()

print(key_phrases)


