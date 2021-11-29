import cv2
import glob

path=glob.glob("C:/Users/Givindu/Desktop/New folder/frames/*.jpg")


for file in path:

    img=cv2.imread(file)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
