import json
import os
import requests
from matplotlib.image import imread
import numpy as np
import urllib.request
import urllib.parse
import time

subscription_key = 'dcce5ed801984189ba69772c802b85b4'
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
headers = { 'Content-Type': 'application/octet-stream','Ocp-Apim-Subscription-Key': subscription_key }

with open('../../sports_cleaned_cricau.json') as f:
	cleaned_data = json.load(f)
    
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender',
}

counter = 0
new_cleaned_data = []
i = 0
print ("Length of cleaned data is",len(cleaned_data))

while i < len(cleaned_data):
	print("Processing for ", i)
	item = cleaned_data[i]
	img_url = item['img_url']
	file_name = item['name'] + item['gender'] + item['age'] + '.jpg'
	full_path = './images_cricau_clean/' + file_name
	data = open(full_path, 'rb')
	response = requests.post(face_api_url, params=params, headers=headers, data=data)
	faces = response.json()
	
	if isinstance(faces, dict): #limit over so sleep till you can start again 
		print("sleeping at",i)
		time.sleep(70)
		continue

	elif len(faces) >= 1:
		print ("This guy's face",item['name'])
		predicted_age = str(faces[0]['faceAttributes']['age'])
		predicted_gender = faces[0]['faceAttributes']['gender'][0].upper()
		item['predicted_age'] = predicted_age
		item['predicted_gender'] = predicted_gender
		new_cleaned_data.append(item)
	
	elif len(faces) == 0:
		print ("Couldnt predict for",item['name'])
		item['predicted_age'] = item['age']
		item['predicted_gender'] = item['gender']
		counter = counter + 1
		new_cleaned_data.append(item)

	with open('../../sports_cleaned_cricau_predicted.json', 'a') as outfile:
		json.dump(item, outfile)
		outfile.write('\n')
	i = i + 1

print("Finished downloading")
print("Count unpredicted ",counter)

