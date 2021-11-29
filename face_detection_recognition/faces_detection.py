import os
import cv2
import numpy as np

size = 2
haar_cascade = cv2.CascadeClassifier('E:/BACKBONE/face_detection_recognition/model/custom_haarcascade.xml')


def registerCriminal(img, path, img_num):
    print("Face Training Started")
    size = 2
    (im_width, im_height) = (112, 92)
    file_num = 2 * img_num - 1

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    if len(faces) > 0:
        # Taking the largest face detected
        faces = sorted(faces, key=lambda x: x[3], reverse=True)  # sort based on height of image
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]

        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (im_width, im_height))

        print("Saving training sample " + str(img_num) + ".1")
        # Save image file
        cv2.imwrite('%s/%s.png' % (path, file_num), face)
        file_num += 1

        # Save flipped image
        print("Saving training sample " + str(img_num) + ".2")
        face = cv2.flip(face, 1, 0)
        cv2.imwrite('%s/%s.png' % (path, file_num), face)

    else:
        # No face present
        print("img %d : Face is not present" % img_num)
        return img_num

    return None


def train_model():
    model = cv2.face.LBPHFaceRecognizer_create()
    fn_dir = 'E:/BACKBONE/face_detection_recognition/Criminals'
    print('Training...')
    (images, lables, names, id) = ([], [], {}, 0)
    print('Train Model Started Running...')
    for (subdirs, dirs, files) in os.walk(fn_dir):
        # Loop through each folder named after the subject in the photos
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)
            # Loop through each photo in the folder
            for filename in os.listdir(subjectpath):
                # Skip non-image formates
                f_name, f_extension = os.path.splitext(filename)
                if f_extension.lower() not in ['.png', '.jpg', '.jpeg', '.gif', '.pgm']:
                    print("Skipping " + filename + ", wrong file type")
                    continue
                path = subjectpath + '/' + filename
                lable = id
                # Add to training data
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1

    # Create a Numpy array from the two lists above
    (images, lables) = [np.array(lis) for lis in [images, lables]]
    # OpenCV trains a model from the images
    model.train(images, lables)
    print("Returning Train_model....")
    return model, names


def detect_faces(gray_frame):
    global size, haar_cascade

    # Resize to speed up detection (optinal, change size above)
    mini_frame = cv2.resize(gray_frame, (int(gray_frame.shape[1] / size), int(gray_frame.shape[0] / size)))

    # Detect faces and loop through each one
    faces = haar_cascade.detectMultiScale(mini_frame)
    return faces


def detect(path):
    # load SSD and ResNet network based caffe model for 300x300 dim imgs
    net = cv2.dnn.readNetFromCaffe("E:/backbone/face_detection_recognition/model/weights-prototxt.txt",
                                   "E:/backbone/face_detection_recognition/model/res_ssd_300Dim.caffeModel")
    cam = cv2.VideoCapture(os.path)

    # loop over video frames
    while True:
        ret, frame = cam.read()

        # convert frame dimensions to a blob and 300x300 dim
        (height, width) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))

        # pass the blob into dnn
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections to extract specific confidence
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # greater than the minimum confidence
            if confidence < 0.5:
                continue

            # compute the boxes (x, y)-coordinates
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x1, y1, x2, y2) = box.astype("int")

            # draw the bounding box of the face along with the associated
            # probability
            text = "{:.2f}%".format(confidence * 100) + " ( " + str(y2 - y1) + ", " + str(x2 - x1) + " )"
            y = y1 - 10 if y1 - 10 > 10 else y1 + 10
            cv2.rectangle(frame, (x1, y1), (x2, y2),
                          (0, 0, 255), 2)
            cv2.putText(frame, text, (x1, y),
                        cv2.LINE_AA, 0.45, (0, 0, 255), 2)

            break
    cam.release()
    cv2.destroyAllWindows()
