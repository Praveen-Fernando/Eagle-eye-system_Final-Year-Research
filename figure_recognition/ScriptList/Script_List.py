import os


# from figure_recognition import imageToVideo
import time


def data(path):
    from figure_recognition import figure
    age, gender = figure.figure(path)
    return age, gender
    # imageToVideo.generate_video()


def figure(path='E:\\BACKBONE\\face_detection_recognition\\output\\Output_Video.avi'):
    from figure_recognition import figure
    age, gender = figure.figure(path)

    time.sleep(80)
    print("Figure recognition completed!")

    return age, gender
    # imageToVideo.generate_video()
