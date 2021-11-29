import cv2
import os
from imageEnhancement import CreateNewFolderForFrames, FramesToVid

from imageEnhancement import Smooth


def removeGaussianNoise(parentFolder, SharpImages, rate):
    GaussianDenoised = CreateNewFolderForFrames.DenoiseGaussian(parentFolder)

    count = 10000000

    for file in os.listdir(SharpImages):
        if file.endswith(".jpg"):
            img = cv2.imread(SharpImages + "\\" + file)

            dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 5)

            cv2.imwrite(GaussianDenoised + "\\%d.jpg" % count, dst)

            count += 1

    # Smooth.imageSmooth(parentFolder, GaussianDenoised)

    value = FramesToVid.generate_video(GaussianDenoised, parentFolder, rate)
    return value
