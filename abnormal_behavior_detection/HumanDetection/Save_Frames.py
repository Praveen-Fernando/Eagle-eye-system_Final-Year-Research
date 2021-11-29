import cv2

cap = cv2.VideoCapture("C:/Users/Givindu/Desktop/New folder/video.mp4")

i = 0
while(cap.isOpened()):
    flag,frame=cap.read()
    if flag==False:
        break

    #save frames
    cv2.imwrite('C:/Users/Givindu/Desktop/New folder/Happy'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

#Hello World