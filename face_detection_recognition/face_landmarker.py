import csv
import os
import dlib
import numpy as np
import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')


# out = cv2.VideoWriter('./face_detection_recognition/output/output.avi', fourcc, 20.0, (1280, 720))


def face_landmark():
    path = cv2.VideoCapture('E:/BACKBONE/videos/Input.mp4')
    print("DETECTING FACIAL LANDMARKS...")
    predictor_path = 'E:/BACKBONE/face_detection_recognition/model/shape_predictor_81_face_landmarks.dat'
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    q = os.path.basename("Facial_Landmarks")
    filename, file_extension = os.path.splitext("E:/BACKBONE/face_detection_recognition/csv/Facial_Landmarks")
    g = filename + '.csv'
    filename = g
    while path.isOpened():
        ret, frame = path.read()
        if ret:
            # filp frame
            frame = cv2.flip(frame, 1)
            dets = detector(frame)
            for k, d in enumerate(dets):
                shape = predictor(frame, d)
                landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
                print("Detected Landmarks : ", landmarks)
                with open(filename, 'w') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(landmarks)
                for num in range(shape.num_parts):
                    cv2.circle(frame, (shape.parts()[num].x, shape.parts()[num].y), 3, (0, 255, 0), -1)

                # Show frame
                # cv2.imshow('frame', frame)
                # out.write(frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     print("----PROCESS COMPLETED----")
                #     break
        else:
            break

    path.release()
    # out.release()
    cv2.destroyAllWindows()
    print("*** STEP 2 EXECUTED SUCCESSFULLY ***")
