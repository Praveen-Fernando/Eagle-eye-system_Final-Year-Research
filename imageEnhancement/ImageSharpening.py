import cv2
import numpy as np
import os
from imageEnhancement import CreateNewFolderForFrames
from imageEnhancement import RemoveGaussianNoise


def imageSharp(parentFolder, ContrastAdjustedFolder, rate):
    SharpImages = CreateNewFolderForFrames.createFolderForSharpImages(parentFolder)

    count = 10000000

    for file in os.listdir(ContrastAdjustedFolder):
        if file.endswith(".jpg"):

            image = cv2.imread(ContrastAdjustedFolder + "\\" + file)

            # kernel_sharpening = np.array([[-1, -1, -1],
            #                               [-1, 9, -1],
            #                               [-1, -1, -1]])

            kernel_sharpening = np.array([[0, -1, 0],
                                          [-1, 5, -1],
                                          [0, -1, 0]])

            # applying the sharpening kernel to the input image & displaying it.
            sharpened = cv2.filter2D(image, -1, kernel_sharpening)

            cv2.imwrite(SharpImages + "\\%d.jpg" % count, sharpened)

            count += 1

    value = RemoveGaussianNoise.removeGaussianNoise(parentFolder, SharpImages, rate)
    return value
