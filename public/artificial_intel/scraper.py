# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from autocorrect import Speller, spell


# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
# 	help="type of preprocessing to be done")
# ap.add_argument("-n", "--name", type=str, default="100")
# args = vars(ap.parse_args())
print("importing file")
image_path = "./picture.jpeg"

# load the example image and convert it to grayscale
image = cv2.imread(image_path)
ratio = 3
new_w = image.shape[1]*ratio
new_h = image.shape[0]*ratio

image = cv2.resize(image, (new_w,new_h), interpolation=cv2.INTER_CUBIC);

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# check to see if we should apply thresholding to preprocess the
# image


# make a check to see if median blurring should be done to remove


# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename), lang='eng', config="--psm 6 --oem 1")
os.remove(filename)

# print(text)
# text = spell(bytestostr(text))
print(text)

print("success")
file = open(str(100)+".txt","w")
file.writelines(text)
file.close()