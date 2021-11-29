# In the previous section, we used a global value as threshold value. But it may not be good in all the conditions where image has different lighting conditions
# in different areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold for a small regions of the image.
# So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.
#
# It has three ‘special’ input params and only one output argument.
#
# Adaptive Method - It decides how thresholding value is calculated.
# cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
# Block Size - It decides the size of neighbourhood area.
#
# C - It is just a constant which is subtracted from the mean or weighted mean calculated.
#
# Below piece of code compares global thresholding and adaptive thresholding for an image with varying illumination:
# Refer : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html  -> Image thresholding

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.jpg',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()