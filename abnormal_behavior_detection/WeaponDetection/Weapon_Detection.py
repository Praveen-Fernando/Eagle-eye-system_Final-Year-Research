import csv
import glob
import os
import time

import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import cv2
import cv2 as cv
import numpy as np
import imutils

count = 1
start = time.time()

def weaponDetection():
    cap = cv.VideoCapture('E:\\BACKBONE`\\abnormal_behavior_detection\\frames\\Generated Video Output\\Output Video.avi')
    whT = 320
    confThreshold = 0.1
    nmsThreshold = 0.1

    directory = 'Suspects with Weapons'
    parent_dir = "E:/BACKBONE/abnormal_behavior_detection/frames/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)


    classesFile = "E:/BACKBONE/abnormal_behavior_detection/Models/Weapon Detection/obj.names"
    classNames = []
    with open(classesFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    print("  ")
    print("STEP 3 ON PROGRESS...")

    ## Model Files
    modelConfiguration = "E:/BACKBONE/abnormal_behavior_detection/Models/Weapon Detection/yolov4-custom.cfg"
    modelWeights = "E:/BACKBONE/abnormal_behavior_detection/Models/Weapon Detection/yolov4-custom_best.weights"
    net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


    def findObjects(outputs, img):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        global count
        Num = 0
        field = ["ID", "Incident Type", "Used Weapon", "Time"]

        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold:
                    w, h = int(det[2] * wT), int(det[3] * hT)
                    x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

        indices = cv.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]


            # Detect handguns
            if classIds[i] == 0:
            # print(x,y,w,h)
                text = "{:.4f}%".format((confs[i])*100)
                print("Suspect Detected : ", "[", text, "]")
                # cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                # cv.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%',
                #           (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

                cv2.imwrite('E:/BACKBONE/abnormal_behavior_detection/frames/Suspects with Weapons/frame%d.jpg' % count, img)
                count += 1

                # Create and save in a CSV File
                type = "Abnormal Activity"
                weapon = "The Pistol was used as a weapon"
                with open('E:/BACKBONE/abnormal_behavior_detection/CSV/Abnormal Activity.csv', 'w', newline='') as file:
                    Num += 1
                    TimeD = time.time() - start
                    arr = [Num, type, weapon, TimeD]
                    writer = csv.writer(file)
                    writer.writerow(field)
                    writer.writerow(arr)



            # Detect knives
            if classIds[i] == '1':
            # print(x,y,w,h)
                text = "{:.4f}%".format((confs[i])*100)
                print("Suspect Detected : ", "[", text, "]")
                #cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                #cv.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%',
                #           (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

                # save detected frames
                cv2.imwrite('E:/BACKBONE/abnormal_behavior_detection/frames/Suspects with Weapons/frame%d.jpg' % count, img)
                count += 1

                # Create and save in a CSV File
                type = "Stabbing Attack"
                weapon = "The Knife was used as a weapon"
                with open('E:/BACKBONE/abnormal_behavior_detection/CSV/Abnormal Activity.csv', 'w', newline='') as file:
                    Num += 1
                    TimeD = time.time() - start
                    arr = [Num, type, weapon, TimeD]
                    writer = csv.writer(file)
                    writer.writerow(field)
                    writer.writerow(arr)



            # Detect grenades
            if classIds[i] == '2':
            # print(x,y,w,h)
                text = "{:.4f}%".format((confs[i])*100)
                print("Suspect Detected : ", "[", text, "]")
                #cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                #cv.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%',
                #           (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

                # save detected frames
                cv2.imwrite('E:/BACKBONE/abnormal_behavior_detection/frames/Suspects with Weapons/frame%d.jpg' % count, img)
                count += 1

                # Create and save in a CSV File
                type = "Abnormal Activity"
                weapon = "The Grenade was used as a weapon"
                with open('E:/BACKBONE/abnormal_behavior_detection/CSV/Abnormal Activity.csv', 'w', newline='') as file:
                    Num += 1
                    TimeD = time.time() - start
                    arr = [Num, type, weapon, TimeD]
                    writer = csv.writer(file)
                    writer.writerow(field)
                    writer.writerow(arr)



    while True:
        success, img = cap.read()
        if success != False:
            img = imutils.resize(img, width=600)
            blob = cv.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
            net.setInput(blob)
            layersNames = net.getLayerNames()
            outputNames = [(layersNames[i[0] - 1]) for i in net.getUnconnectedOutLayers()]
            outputs = net.forward(outputNames)
            findObjects(outputs, img)


            #cv.imshow('Image', img)
            #key = cv2.waitKey(1)
            #if key == ord('q'):
             #   break

        else:
            break

    try:
        conn = msql.connect(host='127.0.0.1', port=3306,
                            database='criminal_investigation', user='root',
                            password='')
        if conn.is_connected():
            # Inserting csv file data to database
            criminalData = pd.read_csv('E:/BACKBONE/abnormal_behavior_detection/CSV/Abnormal Activity.csv', index_col=False, delimiter=',')
            criminalData.head()
            print("  ")
            print(criminalData)
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("  ")
            print("You're connected to database: ", record)
            for i, row in criminalData.iterrows():
                sql = "INSERT INTO criminal_investigation.behavior_details VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                print("Values inserted")
            conn.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)

    cap.release()
    cv2.destroyAllWindows()
    print("  ")
    print("*** ALL STEPS EXECUTED SUCCESSFULLY ***")

# main()
