import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames5\\New Folder\\10000684.jpg'
img1 = cv2.imread(folder)


img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])

img2 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

plt.subplot(221), plt.plot(hist1)
plt.subplot(222), plt.plot(hist2)

scale_percent = 100

width1 = int(img1.shape[1] * scale_percent / 100)
height1 = int(img1.shape[0] * scale_percent / 100)

width2 = int(img2.shape[1] * scale_percent / 100)
height2 = int(img2.shape[0] * scale_percent / 100)

# dsize
dsize1 = (width1, height1)
dsize2 = (width2, height2)

output1 = cv2.resize(img1, dsize1)
output2 = cv2.resize(img2, dsize2)

cv2.imshow("input", output1)
cv2.imshow("EquHist", output2)

cv2.waitKey(0)