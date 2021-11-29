import os

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames13\\10000000.jpg'
# Draw a histogram function

print(folder)

for file in folder:
    img = cv.imread(folder, 1)
    print(file)
    print(type(file))
     # image normalization
    fi = img / 255.0

    gamma = 0.5
    out = np.power(fi, gamma)
    print(out)

cv.imshow("img", img)
cv.imshow("out", out)
cv.imwrite('E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames13\\Enhanced_Frames1\\%d.jpg', out)
cv.waitKey(0)
