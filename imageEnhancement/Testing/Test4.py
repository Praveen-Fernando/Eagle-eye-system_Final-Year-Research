import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames5\\New Folder\\10000157.jpg'
# Draw a histogram function
img = cv.imread(folder, 0)

img = cv.resize(img, None, fx=0.5, fy=0.5)
 #Create a CLAHE object
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
 # Adaptive threshold equalization for limiting contrast
dst = clahe.apply(img)
 # Use global histogram equalization
equa = cv.equalizeHist(img)
 # Show original image, CLAHE, HE
cv.imshow("img", img)
cv.imshow("dst", dst)
cv.imshow("equa", equa)

imgHist = cv2.calcHist(img, [0], None, [256], [0, 256])
dstHist = cv2.calcHist(img, [0], None, [256], [0, 256])
equaHist = cv2.calcHist(img, [0], None, [256], [0, 256])

plt.imshow(imgHist)
cv.waitKey(0)
