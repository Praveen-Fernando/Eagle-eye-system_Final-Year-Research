from face_detection_recognition import criminal_registration
from face_detection_recognition import imageToVideo
from face_detection_recognition import criminal_recognition
from face_detection_recognition import face_landmarker
from face_detection_recognition import db_Handler


def criminalRegistration(id, fileinput):
    reg = criminal_registration.register(id, fileinput)
    print("Criminal Registered", reg)
    return "Registration Done"


# Process_Bar:3rd process
def imagetovideo_process(path):
    vid = imageToVideo.generate_video(path)
    print('vid -> '+vid)
    print("Video passed", path)
    data("E:\\BACKBONE\\face_detection_recognition\\output\\Output_Video.avi")
    return vid


# Individual_Component process
def data(path):
    print("Path passed", path)
    criminal_recognition.train(path)
    face_landmarker.face_landmark()
    db_Handler.return_data()
    print("*** ALL STEPS EXECUTED SUCCESSFULLY ***")
    return "Done"
