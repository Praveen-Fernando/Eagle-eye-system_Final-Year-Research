import cv2

# input video
cap = cv2.VideoCapture("C:/Users/Praveen/Desktop/new/video1.mp4")

i = 0
while cap.isOpened():
    flag, frame = cap.read()
    if flag == False:
        break
    cv2.imwrite('C:/Users/Praveen/Desktop/new/output/frame' + str(i) + '.jpg', frame)
    i += 1

# #Test Commit
