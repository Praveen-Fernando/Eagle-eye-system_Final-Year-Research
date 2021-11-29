import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip
from imageEnhancement import CreateNewFolderForFrames
from imageEnhancement import ContrastEdjustments


def FrameCapture(path):
    print(path)
    folderName = CreateNewFolderForFrames.createFolder()

    print("This is the folder name: " + folderName)

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 10000000

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        if success == 1:
            cv2.imwrite("E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName + "\\%d.jpg" % count, image)

        count += 1

    # loading video dsa gfg intro video
    clip = VideoFileClip(path).subclip(0, 10)

    # getting frame rate of the clip
    rate = clip.fps

    # printing the fps
    print("FPS : " + str(rate))

    print("folder name in Vid to frame : " + folderName)

    value = ContrastEdjustments.adjustContrast(folderName, rate)
    return value
