import os

import cv2
import datetime
import imutils
import numpy as np
#import person_detection_image
from tifffile import askopenfilename


def capture_humans(path):

    # path = "E:\\BACKBONE\\videos\\Input.mp4"
    print(path)

    protopath = "E:/BACKBONE/abnormal_behavior_detection/Models/Human Detection/MobileNetSSD_deploy.prototxt"
    modelpath = "E:/BACKBONE/abnormal_behavior_detection/Models/Human Detection/MobileNetSSD_deploy.caffemodel"
    detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)
    # Only enable it if you are using OpenVino environment
    # detector.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
    # detector.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    CLASSES = []
    classFile = 'E:/BACKBONE/abnormal_behavior_detection/Models/Human Detection/class.names'
    with open(classFile, 'rt') as f:
        CLASSES = f.read().rstrip('\n').split('\n')

    print("STEP 1 ON PROGRESS...")


    #Get input video
    cap = cv2.VideoCapture(path)

    #Interface Window
    #imgTemp = askopenfilename(title="Choose a video")
    #cap = cv2.VideoCapture(imgTemp)

    directory = 'All Detected Humans'
    parent_dir = "E:/BACKBONE/abnormal_behavior_detection/frames/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)


    fps_start_time = datetime.datetime.now()
    fps = 0
    total_frames = 0
    count = 100000
    while True:
        ret, frame = cap.read()
        if ret != False:
            frame = imutils.resize(frame, width=1000)
            total_frames = total_frames + 1

            (H, W) = frame.shape[:2]

            blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

            detector.setInput(blob)
            person_detections = detector.forward()

            for i in np.arange(0, person_detections.shape[2]):
                confidence = person_detections[0, 0, i, 2]
                if confidence > 0.5:
                    idx = int(person_detections[0, 0, i, 1])

                    if CLASSES[idx] != "person":
                        continue

                    person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                    (startX, startY, endX, endY) = person_box.astype("int")

                    text = "{:.4f}%".format(confidence * 100)
                    #put rectangle
                    #cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
                    #cv2.putText(frame, CLASSES, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

                    #crop detected frames
                    crop = frame[startY:endY, startX:endX]

                    if CLASSES[idx] == "person":
                        print("Human Detected : ", "[", text, "]")
                        if crop.size != 0:
                            cv2.imwrite('E:/BACKBONE/abnormal_behavior_detection/frames/All Detected Humans/frame'+str(count)+'.jpg', crop)
                            count += 1

            #Add fps count#
            fps_end_time = datetime.datetime.now()
            time_diff = fps_end_time - fps_start_time
            if time_diff.seconds == 0:
                fps = 0.0
            else:
                fps = (total_frames / time_diff.seconds)

            fps_text = "FPS: {:.2f}".format(fps)

            cv2.putText(frame, fps_text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

            #Output Window
            #cv2.imshow("Application", frame)
            #key = cv2.waitKey(1)
            #if key == ord('q'):
             #   break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    print(" ")
    print("*** STEP 1 EXECUTED SUCCESSFULLY ***")

#main(path)
#print(" ")
#print("*** STEP 1 EXECUTED SUCCESSFULLY ***")
#person_detection_image.main()
#FramesToVideo.frames()