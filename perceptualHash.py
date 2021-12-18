import os
import cv2
from PIL import Image
import imagehash
import numpy
import scipy
import scipy.fftpack


TARGET_FILE = '/Users/odyss/Documents/Leafhub/work/clairvision/imageHash/pict/01/IMG_0023_BURST00120211210142515.JPG'
IMG_DIR = '/Users/odyss/Documents/Leafhub/work/clairvision/imageHash/pict/'
target_img_path = IMG_DIR + TARGET_FILE
target_hash = imagehash.average_hash(Image.open(target_img_path))
files = os.listdir(IMG_DIR)

print('TARGET_FILE: %s' % (TARGET_FILE), target_hash)
print('files: %s' % (files))
for file in files:
    if file == '.DS_Store' or file == TARGET_FILE:
        continue

    comparing_img_path = IMG_DIR + file
    try:
        hash = imagehash.average_hash(Image.open(comparing_img_path))
        haming = target_hash - hash
    except cv2.error:
        ret = 100000

    print(file, hash, haming)