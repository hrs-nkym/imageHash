from PIL import Image
import numpy as np
import glob
import os
import matplotlib.pyplot as plt

size = 64
target_file = r"./pict/IMG_0023_BURST00120211210142515.JPG"
search_dir = r"./pict/"

# 画像データをAverage hashに変換
def average_hash(target_file, size=8):
    img = Image.open(target_file).convert("L")  # Image.Openで画像ファイルをオープン
    img = img.resize((size, size), Image.ANTIALIAS)  # グレースケール変換＆アンチエイリアス処理で圧縮
    img = np.array(img)  # 画素データを取得してリサイズ
    avg = img.mean()  # 画素値の平均値を取得
    px = 1 * (img > avg)  # 画素データ（px）で平均より大きい要素を1に、それ以外は0に変換
    return px


# 画像データをAverage hashに変換
def hamming_dist(a, b):
    a = a.reshape(1, -1)  # 1行のベクトルに変換
    b = b.reshape(1, -1)  # 1行のベクトルに変換
    dist = (a != b).sum()  # 要素が異なる場合は1を加算していく
    return dist
