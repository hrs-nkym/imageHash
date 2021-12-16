from PIL import Image
import imagehash


def diff(img1, img2):
    hash1 = imagehash.phash(Image.open(img1))
    hash2 = imagehash.phash(Image.open(img2))
    return hash1 - hash2


for target in [
    "./pict/IMG_0023_BURST00120211210142515.JPG",
    "./pict/IMG_0023_BURST00120211210143047.JPG",
    "./pict/IMG_0023_BURST00120211210143338.JPG",
    "./pict/IMG_0023_BURST00120211210144234.JPG",
]:
    print(
        "%s=%s" % (target, diff("./pict/IMG_0023_BURST00120211210142515.JPG", target))
    )
