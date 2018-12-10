import json
import os
import requests
from matplotlib.image import imread
import numpy as np
import urllib.request
import urllib.parse
import cv2

template_img  = imread('./images_cricau/abul-hasanM26.jpg')
template_img2 = imread('./images_cricau/lea-tahuhuF28.jpg')
template_img3 = imread('./images_cricau/matilda-luggFTBD.jpg')
template_img4 = imread('./images_cricau/timm-van-der-gugtenM27.jpg')



def clean_img(file_name):
	fullPath = './images_cricau/'+file_name
	img = imread(fullPath)
	return np.array_equal(img,template_img) or np.array_equal(img,template_img2) or np.array_equal(img,template_img3) or np.array_equal(img,template_img4)

def download_img_and_resize(img_url, file_name):
	full_path = './images_cricau_clean/' + file_name
	print("Saving in ",full_path)
	encoded_url = urllib.parse.quote(img_url)
	encoded_url = encoded_url.replace("%3A",":")
	print(encoded_url)
	urllib.request.urlretrieve(encoded_url,full_path)
	image = cv2.imread(full_path)
	resized_image = cv2.resize(image,(192, 192), interpolation = cv2.INTER_CUBIC)
	cv2.imwrite(full_path,resized_image)

with open('../../cricau.json') as f:
	data = json.load(f)

cleaned_data = []
for item in data:
	img_url = item['img_url']
	file_name = item['name'] + item['gender'] + item['age'] + '.jpg'
	if clean_img(file_name) == False:
		cleaned_data.append(item)
		download_img_and_resize(img_url,file_name)



with open('../../sports_cleaned_cricau.json', 'w') as outfile:
		json.dump(cleaned_data, outfile)

print("finished writing")
print("Length of cleaned_data",len(cleaned_data))












