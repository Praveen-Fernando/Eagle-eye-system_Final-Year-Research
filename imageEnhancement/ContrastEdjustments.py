import cv2
import os

from imageEnhancement import ImageSharpening
from imageEnhancement import CreateNewFolderForFrames


def adjustContrast(folder, rate):
    contrastAdjustedFrames = CreateNewFolderForFrames.createFolderForContrasted(folder)

    path = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folder

    count = 10000000

    for file in os.listdir(path):
        if file.endswith(".jpg"):
            # -----Reading the image-----------------------------------------------------
            img = cv2.imread(path + "\\" + file)

            # -----Converting image to LAB Color model-----------------------------------
            lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

            # -----Splitting the LAB image to different channels-------------------------
            l, a, b = cv2.split(lab)

            # -----Applying CLAHE to L-channel-------------------------------------------
            clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(1, 1))
            cl = clahe.apply(l)

            # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
            limg = cv2.merge((cl, a, b))

            # -----Converting image from LAB Color model to RGB model--------------------
            final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

            cv2.imwrite(contrastAdjustedFrames + "\\%d.jpg" % count, final)

            count += 1

    value = ImageSharpening.imageSharp(folder, contrastAdjustedFrames, rate)
    return value
