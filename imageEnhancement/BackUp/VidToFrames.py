# Program To Read video
# and Extract Frames
import cv2
from moviepy.editor import *

# Function to extract frames
import CreateNewFolderForFrames
import FramesToVid


def FrameCapture(path):

    folderName = CreateNewFolderForFrames.createFolder()

    print("This is the folder name: "+folderName)
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
        # cv2.imwrite("E:\\#ProgrammingWork\\Python\\VideoEnhance\\a\\frame%d.jpg" % count, image)
        if success == 1:
            cv2.imwrite("E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\"+folderName+"\\%d.jpg" % count, image)

        count += 1

    # loading video dsa gfg intro video
    clip = VideoFileClip("E:\\#ProgrammingWork\\Python\\VideoEnhance\\vid\\video4.mp4").subclip(0, 10)

    # getting frame rate of the clip
    rate = clip.fps

    # printing the fps
    print("FPS : " + str(rate))

    FramesToVid.generate_video(folderName,rate)


# Driver Code
if __name__ == '__main__':

    # Calling the function
    FrameCapture("E:\\#ProgrammingWork\\Python\\VideoEnhance\\vid\\video4.mp4")
