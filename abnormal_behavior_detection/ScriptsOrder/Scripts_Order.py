import os
from abnormal_behavior_detection.FramesConverter import Frames_To_Video
from abnormal_behavior_detection.WeaponDetection import Weapon_Detection
from abnormal_behavior_detection.HumanDetection import Human_Detection_Video

def data(path):

    print("AB path -> "+path)

    file = path.split("\\")[2]

    if file == "Enhanced_Video.avi":
        path = path
    elif file == "Input.avi":
        path = "E:\\BACKBONE\\videos\\" + file
    elif file == "Input.mp4":
        path = "E:\\BACKBONE\\videos\\" + file

    print("path ->" + path)

    Human_Detection_Video.capture_humans(path)
    Frames_To_Video.framesConverter()
    Weapon_Detection.weaponDetection()

    return "Done"

    # os.system('python ../HumanDetection/Human_Detection_Video.py')
    # os.system('python ../FramesConverter/Frames_To_Video.py')
    # ##os.system('python ../FramesConverter/Frames_To_Video_Test.py')
    # os.system('python ../WeaponDetection/Weapon_Detection.py')
