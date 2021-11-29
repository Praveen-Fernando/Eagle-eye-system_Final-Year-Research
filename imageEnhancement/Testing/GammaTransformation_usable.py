import os

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

folder = 'E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames13'
# Draw a histogram function

print(folder)

count = 10000000

for file in os.listdir(folder):
    img = cv.imread('E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames13\\'+file, 1)
    print(img)
    print(file)
    #print(type(img))
    # image normalization
    fi = img / 255.0

    gamma = 1.0
    out = np.power(fi, gamma)
    print(out)
    cv.imwrite('E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames13\\Enhanced_Frames1\\%d.jpg' % count, out)
    count+=1
# cv.imshow("img", img)
# cv.imshow("out", out)
cv.waitKey(0)
