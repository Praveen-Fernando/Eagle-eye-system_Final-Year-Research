import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames5\\New Folder\\10000157.jpg'
img = cv2.imread(folder, 0)

hist1 = cv2.calcHist([img], [0], None, [256], [0, 256])

equlizedImg = cv2.equalizeHist(img)

hist2 = cv2.calcHist([equlizedImg], [0], None, [256], [0, 256])

plt.subplot(221), plt.plot(hist1)
plt.subplot(222), plt.plot(hist2)

result = np.hstack((img, equlizedImg))
plot = np.hstack((hist1, hist2))
cv2.imshow("result", result)
cv2.waitKey(0)