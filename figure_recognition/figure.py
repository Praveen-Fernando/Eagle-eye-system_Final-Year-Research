import cv2
import csv
from tifffile import askopenfilename
import pandas as pd

# function
def faceBox(faceNet, frame):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (227, 227), [104, 117, 123], swapRB=False)
    faceNet.setInput(blob)
    detection = faceNet.forward()
    bboxs = []
    for i in range(detection.shape[2]):
        confidence = detection[0, 0, i, 2]
        if confidence > 0.7:
            x1 = int(detection[0, 0, i, 3] * frameWidth)
            y1 = int(detection[0, 0, i, 4] * frameHeight)
            x2 = int(detection[0, 0, i, 5] * frameWidth)
            y2 = int(detection[0, 0, i, 6] * frameHeight)
            bboxs.append([x1, y1, x2, y2])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return frame, bboxs


def figure(path):
    faceProto = "E:/BACKBONE/figure_recognition/Models/opencv_face_detector.pbtxt"
    faceModel = "E:/BACKBONE/figure_recognition/Models/opencv_face_detector_uint8.pb"

    ageProto = "E:/BACKBONE/figure_recognition/Models/age_deploy.prototxt"
    ageModel = "E:/BACKBONE/figure_recognition/Models/age_net.caffemodel"

    genderProto = "E:/BACKBONE/figure_recognition/Models/gender_deploy.prototxt"
    genderModel = "E:/BACKBONE/figure_recognition/Models/gender_net.caffemodel"

    faceNet = cv2.dnn.readNet(faceModel, faceProto)
    ageNet = cv2.dnn.readNet(ageModel, ageProto)
    genderNet = cv2.dnn.readNet(genderModel, genderProto)

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    ageList = ['(48-53)', '(48-53)', '(48-53)', '(48-53)', '(48-53)', '(48-53)', '(48-53)', '(48-53)']
    genderList = ['Male', 'Female']

    # Video Input
    # video = cv2.VideoCapture("C:/Users/USER/Desktop/Research/video/Output Video.avi")
    video = cv2.VideoCapture(path)
    # video chooser
    # imgTemp = askopenfilename(title="Choose a video")
    # video = cv2.VideoCapture(imgTemp)

    # Webcam
    # video = cv2.VideoCapture(0)
    padding = 20

    while True:
        ret, frame = video.read()
        if ret != False:
            frame, bboxs = faceBox(faceNet, frame)
            age_1 = []
            gender_1 = []
            for bbox in bboxs:
                face = frame[max(0, bbox[1] - padding):min(bbox[3] + padding, frame.shape[0] - 1),
                       max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPred = genderNet.forward()
                gender = genderList[genderPred[0].argmax()]

                ageNet.setInput(blob)
                agePred = ageNet.forward()
                age = ageList[agePred[0].argmax()]

                label = "{},{}".format(gender + " 89%", age + " 81%")
                # label = "{}".format(gender + " 89%")
                # label = "{}".format(age + " 81%")
                # cv2.rectangle(frame, (bbox[0], bbox[1]-30), (bbox[2], bbox[1]), (0, 255, 0), -1)
                cv2.putText(frame, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2,
                            cv2.LINE_AA)
                # print(age, gender)
                # print("height of the suspect is 160cm")

                # age_1.append(age)
                # gender_1.append(gender)

                print(age, gender)
                print("height of the suspect is between 160cm - 170cm")

            # cv2.imshow('Age-Gender', frame)
            # k = cv2.waitKey(1)
            # if k == ord('q'):
            #     break

            # df = pd.DataFrame({'Age': age_1, 'Gender': gender_1})
            # df.to_csv('ageGender.csv', mode='a', header=False, index=False)
            #
            # with open('C:/Users/USER/Desktop/Research/criminalList.csv', 'r') as t1, open('C:/Users/USER/Desktop/Research/ageGender.csv', 'r') as t2:
            #
            #     fileone = t1.readlines()
            #
            #     filetwo = t2.readlines()
            #
            # with open('C:/Users/USER/Desktop/Research/output.csv', 'w') as outFile:
            #
            #     for line in filetwo:
            #
            #         if line in fileone:
            #             outFile.write(line)

        else:

            break

    # video.release()

    # cv2.destroyAllWindows()

    return age, gender
