import glob
import faces_recognition
import argparse
import pickle
import cv2
import os

imagepaths = []
for name in glob.glob("dataset/*"):
    imagepaths.append(name)

data = []
for (i, img) in enumerate(imagepaths):
    print("img {}/{} ".format(i + 1, len(imagepaths)))
    imgg = cv2.imread(img)
    rgb = cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB)
    boxes = faces_recognition.face_locations(rgb)
    encodings = faces_recognition.face_encodings(rgb, boxes)
    d = [{"imgpath": img, "box": box, "encodings": enc} for (box, enc) in zip(boxes, encodings)]
    data.extend(d)

f = open("E:/BACKBONE/face_detection_recognition/model/enc.picke", "wb")
f.write(pickle.dumps(data))
f.close()
