import urllib.request
import os
import json
import urllib.parse
import cv2

def download_img(img_url, file_name):
	full_path = './images_cricau/' + file_name
	print("Saving in ",full_path)
	encoded_url = urllib.parse.quote(img_url)
	encoded_url = encoded_url.replace("%3A",":")
	print(encoded_url)
	urllib.request.urlretrieve(encoded_url,full_path)

def download_img_and_resize(img_url, file_name):
	full_path = './images_cricau_clean/' + file_name
	print("Saving in ",full_path)
	encoded_url = urllib.parse.quote(img_url)
	encoded_url = encoded_url.replace("%3A",":")
	print(encoded_url)
	urllib.request.urlretrieve(encoded_url,full_path)
	image = cv2.imread(full_path)
	resized_image = cv2.resize(image,(192, 192))
	cv2.imwrite(full_path,resized_image)

with open('../../cricau.json') as f:
	data = json.load(f)

for item in data:
	img_url = item['img_url']
	file_name = item['name'] + '_' + item['gender'] + '_' + item['age'] + '.jpg'
	download_img_and_resize(img_url,file_name)

print("finished downloading")