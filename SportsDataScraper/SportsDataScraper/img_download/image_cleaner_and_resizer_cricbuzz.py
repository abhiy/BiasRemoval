import json
import os
import requests
from matplotlib.image import imread
import numpy as np
import urllib.request
import urllib.parse
import cv2

template_img  = imread('./images/Nazmus Sadat_M_32.jpg')

def clean_img(file_name):
	fullPath = './images/'+file_name
	img = imread(fullPath)
	return np.array_equal(img,template_img)

def download_img_and_resize(img_url, file_name):
	full_path = './images_cricbuzz_clean/' + file_name
	print("Saving in ",full_path)
	encoded_url = urllib.parse.quote(img_url)
	encoded_url = encoded_url.replace("%3A",":")
	print(encoded_url)
	urllib.request.urlretrieve(encoded_url,full_path)
	image = cv2.imread(full_path)
	resized_image = cv2.resize(image,(192, 192), interpolation = cv2.INTER_CUBIC)
	cv2.imwrite(full_path,resized_image)

with open('../../sports.json') as f:
	data = json.load(f)

cleaned_data = []
for item in data:
	img_url = item['img_url']
	file_name = item['name'] + '_' + item['gender'] + '_' + item['age'] + '.jpg'
	if clean_img(file_name) == False:
		cleaned_data.append(item)
		download_img_and_resize(img_url,file_name)



with open('../../sports_cleaned.json', 'w') as outfile:
		json.dump(cleaned_data, outfile)

print("finished writing")
print("Length of cleaned_data",len(cleaned_data))












