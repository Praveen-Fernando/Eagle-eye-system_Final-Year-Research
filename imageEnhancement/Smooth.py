import cv2
import os

from imageEnhancement import CreateNewFolderForFrames


def imageSmooth(parentFolder, GaussianDenoised):
    smooth = CreateNewFolderForFrames.smoothImagesFolder(parentFolder)

    count = 10000000

    for file in os.listdir(GaussianDenoised):
        if file.endswith(".jpg"):
            img = cv2.imread(GaussianDenoised + "\\" + file)

            blur = cv2.bilateralFilter(img, 60, 90, 90)

            cv2.imwrite(smooth + "\\%d.jpg" % count, blur)

            count += 1


# if __name__ == '__main__':
#     imageSmooth("Frames1", "E:\\BACKBONE\\image_enhancement\\Frames\\Frames1\\Sharp_Frames2")
