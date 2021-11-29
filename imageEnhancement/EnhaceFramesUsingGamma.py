import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

from imageEnhancement import CreateNewFolderForFrames
from imageEnhancement import FramesToVid


def enhanceFrames(folderName, frameRate):
    print("Folder name : " + folderName)

    enhancedFolderName = "Enhanced_Frames1"

    #print("Folder path : "+str(folderPath))
    print("enhancedFolderName path : "+enhancedFolderName)

    count = 10000000

    folder = os.chdir('E:\\BACKBONE\\image_enhancement\\Frames\\'+folderName)
    # Draw a histogram function

    print(folder)

    for file in os.listdir(folder):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            img = cv.imread(file, 1)
            # print(img)
            # image normalization
            fi = img / 255.0

            gamma = 0.5
            out = np.power(fi, gamma)
            print(out)
            cv.imwrite('E:\\BACKBONE\\image_enhancement\\Frames\\'+folderName+'\\' + enhancedFolderName + '\\%d.jpg' % count,out)
        count += 1


    #FramesToVid.generate_video(folderName, frameRate)

if __name__ == '__main__':
    enhanceFrames("Frames1",60)