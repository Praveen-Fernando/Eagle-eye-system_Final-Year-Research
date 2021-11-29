import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames5\\New Folder\\10000157.jpg'

def calcGrayHist(I):
    # Calculate the gray histogram
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
    return grayHist


img = cv.imread(folder, 0)
grayHist = calcGrayHist(img)
x = np.arange(256)
# Draw a grayscale histogram
plt.plot(x, grayHist, 'r', linewidth=2, c='black')
plt.xlabel("gray Label")
plt.ylabel("number of pixels")
plt.show()
cv2.imshow("img",img)
cv2.waitKey(0)
