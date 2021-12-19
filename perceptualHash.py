import os
import cv2
from PIL import Image
import imagehash
import numpy
import scipy
import scipy.fftpack


TARGET_FILE = 'IMG_0023_BURST00120211210142554.JPG'
IMG_DIR = './pict/'
target_img_path = IMG_DIR + TARGET_FILE
# target_hash = imagehash.average_hash(Image.open(target_img_path))
target_hash = imagehash.phash(Image.open(target_img_path))
# target_hash = imagehash.dhash(Image.open(target_img_path))
# target_hash = imagehash.whash(Image.open(target_img_path))
files = os.listdir(IMG_DIR)

print('TARGET_FILE: %s' % (TARGET_FILE), target_hash)
print('files: %s' % (files))

for file in files:
    if file == TARGET_FILE:
        continue

    comparing_img_path = IMG_DIR + file
    try:
        # hash = imagehash.average_hash(Image.open(comparing_img_path))
        hash = imagehash.phash(Image.open(comparing_img_path))
        # hash = imagehash.dhash(Image.open(comparing_img_path))
        # hash = imagehash.whash(Image.open(comparing_img_path))
        haming = target_hash - hash
    except cv2.error:
        ret = 100000

    print(file, hash, haming)