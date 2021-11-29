import math

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames5\\New Folder\\10000157.jpg'
# Draw a histogram function
img = cv.imread(folder, 0)

def calcGrayHist(I):
    # Calculate the gray histogram
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
            return grayHist


def equalHist(img):
    # Gray image matrix height and width
    h, w = img.shape
    # : Calculate the gray histogram
    grayHist = calcGrayHist(img)
    #  : Calculating the cumulative gray histogram
    zeroCumuMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p - 1] + grayHist[p]
        # Third step: According to the cumulative gray histogram, the mapping relationship between the input gray level and the output gray level is obtained.
    outPut_q = np.zeros([256], np.uint8)
    cofficient = 256.0 / (h * w)
    for p in range(256):
        q = cofficient * float(zeroCumuMoment[p]) - 1
        if q >= 0:
            outPut_q[p] = math.floor(q)
        else:
            outPut_q[p] = 0
        # Step 4: Get the histogram equalized image
    equalHistImage = np.zeros(img.shape, np.uint8)
    for i in range(h):
        for j in range(w):
            equalHistImage[i][j] = outPut_q[img[i][j]]
    return equalHistImage


# Use your own function to achieve
equa = equalHist(img)
# grayHist(img, equa)
# Using the histogram equalization function provided by OpenCV
# equa = cv.equalizeHist(img)
cv.imshow("img", img)
cv.imshow("equa", equa)
cv.waitKey()