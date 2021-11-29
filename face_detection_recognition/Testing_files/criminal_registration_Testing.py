import shutil
from face_detection_recognition.faces_detection import *


def register(id, fileinput):
    images = list()
    for path in os.listdir(fileinput):
        if '.jpg' in path:  # this could be more correctly done with os.path.splitext
            image = cv2.imread(os.path.join(fileinput, path))
            if image is not None:
                images.append(image)

    # Setting Directory
    path = os.path.join('C:/Users/Praveen/Desktop/new/Criminals', "temp_criminal")
    if not os.path.isdir(path):
        os.mkdir(path)

    no_face = []
    for i, img in enumerate(images):
        # Storing Images in directory
        registerCriminal(img, path, i + 1)

    # check if any image doesn't contain face
    if len(no_face) > 0:
        no_face_st = ""
        for i in no_face:
            no_face_st += "Image " + str(i) + ", "
            print("Registration Error", "Registration failed!\n\nFollowing images doesn't contain"
                                        " face or Face is too small:\n\n%s" % no_face_st)
            shutil.rmtree(path, ignore_errors=True)

    else:
        rowId = 1
        if rowId >= 0:
            print("Successfully Trained")
            shutil.move(path, os.path.join('C:/Users/Praveen/Desktop/new/Criminals', str(id)))


cv2.destroyAllWindows()

fileinput = 'C:\\Users\\Praveen\\Desktop\\new\\output'
register(4, fileinput)