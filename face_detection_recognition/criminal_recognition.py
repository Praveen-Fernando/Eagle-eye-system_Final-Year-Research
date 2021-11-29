import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
from face_detection_recognition.faces_detection import *
from face_detection_recognition.faces_recognition import *
import threading
import os
import time
import csv


def videoLoop(path, model, names):
    path = cv2.VideoCapture(path)
    print("Video loop Function Started")
    q = os.path.basename("Criminals")
    filename, file_extension = os.path.splitext("E:/BACKBONE/face_detection_recognition/csv/Criminals")
    start = time.time()
    times = []
    old_recognized = []
    crims_found_labels = []
    field = ['S.No.', 'cID', 'Time']
    g = filename + '.csv'
    filename = g
    num = 0
    try:
        while not thread_event.is_set():
            while True:
                # Put the image from the webcam into 'frame'
                (return_val, frame) = path.read()
                if return_val == True:
                    break

            # Flip the image (optional)
            frame = cv2.flip(frame, 1, 0)
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect Faces
            face_coords = detect_faces(gray_frame)
            (frame, recognized) = recognize_face(model, frame, gray_frame, face_coords, names)
            # print("----Detecting face----",names)

            # Recognize Faces
            recog_names = [item[0] for item in recognized]
            if recog_names != old_recognized:
                del (crims_found_labels[:])

                for i, crim in enumerate(recognized):
                    with open(filename, 'w') as csvfile:
                        num += 1
                        x = time.time() - start
                        y = crim[0]
                        print(x, y)
                        arr = [num, y, x]
                        # peoplewriter.writerow(arr)
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(field)
                        csvwriter.writerow(arr)

                # print('hello')
                old_recognized = recog_names
                # print(old_recognized)
                # cv2.imshow("Frame", frame)
                break

    except RuntimeError:
        print("Caught Runtime Error")
        print("Caught Error")

    try:
        conn = msql.connect(host='127.0.0.1', port=3306,
                            database='criminal_investigation', user='root',
                            password='')
        if conn.is_connected():
            # Inserting csv file data to database
            criminalData = pd.read_csv('E:/BACKBONE/face_detection_recognition/csv/Criminals.csv', index_col=False, delimiter=',')
            criminalData.head()
            cursor = conn.cursor()
            cursor.execute("select database();")
            cursor.fetchone()
            # print("database connected")
            cursor.execute("DROP TABLE IF EXISTS criminals;")
            # print("Existing Table Dropped")
            cursor.execute("CREATE TABLE criminals(SNo int(10) NOT NULL, cID int(10) NOT NULL, Time float NOT NULL)")
            # print("Criminal Result Table Created")
            for i, row in criminalData.iterrows():
                sql = "INSERT INTO criminal_investigation.criminals VALUES (%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Criminal's Record inserted")
            conn.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)

    path.release()
    cv2.destroyAllWindows()
    print("*** STEP 1 EXECUTED SUCCESSFULLY ***")


def train(path):
    global thread_event
    (model, names) = train_model()
    print('Training Process Success... Detecting Faces.....')
    thread_event = threading.Event()
    thread = threading.Thread(target=videoLoop, args=(path, model, names))
    thread.start()
    print('Detecting & Recognizing Faces.....')
    cv2.destroyAllWindows()
