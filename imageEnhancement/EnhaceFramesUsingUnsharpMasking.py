import cv2 as cv2
import os
import matplotlib.pyplot as plt

from imageEnhancement import CreateNewFolderForFrames
from imageEnhancement import FramesToVid


def enhanceFrames(folderName, rate):

    enhancedPath = CreateNewFolderForFrames.createFolderForEnhancedFrames(folderName)

    path = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName
    print("path : " + path)
    print("enhancedPath : " + enhancedPath)

    count = 10000000

    for file in os.listdir(path):
        if file.endswith(".jpg"):
            image = cv2.imread(path + "\\" + file)
            gaussian_3 = cv2.GaussianBlur(image, (0, 0), 3.0)
            unsharp_image = cv2.addWeighted(image, 5, gaussian_3, -3.5, 0, image)
            cv2.imwrite("E:\\BACKBONE\\image_enhancement\\Frames\\"+folderName+"\\"+enhancedPath+"\\%d.jpg" % count, unsharp_image)
            count += 1

    value = FramesToVid.generate_video(folderName, enhancedPath, rate)
    return value
