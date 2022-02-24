#!/usr/bin/env python
# coding=utf-8
import request
import json
 
# Configure API access
apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
sentimentUri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
keyPhrasesUri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases'
languageUri = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/languages'


# Ask the user for a text
print('Enter a text (or leave blank for default text)')
sampleText = input()
if (sampleText == ''):
    sampleText = 'I really love Azure. It is the best cloud platform.'
# Prepare headers
headers = {}
headers['Ocp-Apim-Subscription-Key'] = apiKey
headers['Content-Type'] = 'application/json'
headers['Accept'] = 'application/json'
# Detect language
postData1 = json.dumps({"documents":[{"id":"1", "text":sampleText}]}).encode('utf-8')
request1 = urllib.request.Request(languageUri, postData1, headers)
response1 = urllib.request.urlopen(request1)
response1json = json.loads(response1.read().decode('utf-8'))
language = response1json['documents'][0]['detectedLanguages'][0]['iso6391Name'] # Sample json: {'errors': [], 'documents': [{'id': '1', 'detectedLanguages': [{'name': 'English', 'score': 1.0, 'iso6391Name': 'en'}]}]}
 
# Determine sentiment
postData2 = json.dumps({"documents":[{"id":"1", "language":language, "text":sampleText}]}).encode('utf-8')
request2 = urllib.request.Request(sentimentUri, postData2, headers)
response2 = urllib.request.urlopen(request2)
response2json = json.loads(response2.read().decode('utf-8'))
sentiment = response2json['documents'][0]['score'] # Sample json: {'errors': [], 'documents': [{'id': '1', 'score': 0.946106320818458}]}
 
# Determine key phrases
postData3 = postData2
request3 = urllib.request.Request(keyPhrasesUri, postData3, headers)
response3 = urllib.request.urlopen(request3)
response3json = json.loads(response3.read().decode('utf-8'))
keyPhrases = response3json['documents'][0]['keyPhrases'] # Sample json: {'documents': [{'keyPhrases': ['Azure'], 'id': '1'}], 'errors': []}



#Display results
print('Text: %s' % sampleText)
print('Language: %s' % language)
print('Sentiment: %f' % sentiment)
print('Key phrases: %s' % keyPhrases)
