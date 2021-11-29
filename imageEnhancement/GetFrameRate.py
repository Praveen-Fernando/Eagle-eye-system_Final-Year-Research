# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("E:\\#ProgrammingWork\\pyCharm\\imageEnhancement\\vid\\video2.mp4").subclip(0, 10)

# getting frame rate of the clip
rate = clip.fps

# printing the fps
print("FPS : " + str(rate))


print("---------------------------------------")






