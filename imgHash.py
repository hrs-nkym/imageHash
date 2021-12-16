import os
from typing import Dict
from PIL import Image
import imagehash

userpath = "./pict/"  # 検索するパス

image_files = []
f = [os.path.join(userpath, path) for path in os.listdir(userpath)]
for i in f:
    if i.endswith(".JPG"):
        image_files.append(i)

imgs: Dict = {}
for img in sorted(image_files):
    # hash = imagehash.average_hash(Image.open(img))  # 33 165 3367
    # hash = imagehash.phash(Image.open(img)) # 25 125 2551
    # hash = imagehash.dhash(Image.open(img))  # 9      45     919
    hash = imagehash.whash(Image.open(img))  # 36     180    3673
    if hash in imgs:
        print("Similar image :", img, imgs[hash])
    else:
        imgs[hash] = img
