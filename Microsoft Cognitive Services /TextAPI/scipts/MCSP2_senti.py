#!/usr/bin/env python
# coding=utf-8
import requests
import sys 
import json 
reload(sys)
sys.setdefaultencoding('utf8')


#print(sys.argv[0])
#print(sys.argv[1])

subscription_key = '***********'
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"

sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

Documents=json.load(open('test1.json'))

#print(Documents)
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=Documents)
sentiments = response.json()

print(sentiments)





