import cv2
import os

image = cv2.imread("E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames7")

os.chdir("E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames7")
path = "E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames7"

count = 10000000

for file in os.listdir(path):
    if file.endswith(".jpg"):
        image = cv2.imread("E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames7\\"+file)
        gaussian_3 = cv2.GaussianBlur(image, (0, 0), 2.0)
        unsharp_image = cv2.addWeighted(image, 7, gaussian_3, -3.5, 0, image)
        cv2.imwrite("E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\Frames7\\Enhanced\\%d.jpg" % count, unsharp_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        count+=1
