# importing libraries
import os
import cv2
from PIL import Image

# Video Generating function
from imageEnhancement import CreateNewFolderForVideos


def generate_video(folderName, parentFolder, rate):
    print("Image folder : " + folderName)
    print("parentFolder : " + parentFolder)
    video_folder_name = "video_" + folderName.split('\\')[5]

    video_folder_path = CreateNewFolderForVideos.createFolderForEnhancedVideos()

    # path = "E:\\BACKBONE\\image_enhancement\\Frames\\"+folderName+"\\"+enhancedPath
    path = folderName

    mean_height = 0
    mean_width = 0

    num_of_images = len(os.listdir('.'))
    # print(num_of_images)

    for file in os.listdir(path):
        im = Image.open(os.path.join(path, file))
        width, height = im.size
        mean_width += width
        mean_height += height
    # im.show() # uncomment this for displaying the image

    # Finding the mean height and width of all images.
    # This is required because the video frame needs
    # to be set with same width and height. Otherwise
    # images not equal to that width height will not get
    # embedded into the video
    mean_width = int(mean_width / num_of_images)
    mean_height = int(mean_height / num_of_images)

    # Resizing of the images to give
    # them same width and height
    for file in os.listdir('.'):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            # opening image using PIL Image
            im = Image.open(os.path.join(path, file))

            # im.size includes the height and width of image
            width, height = im.size
            print(width, height)

            # resizing
            imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
            imResize.save(file, 'JPEG', quality=100)  # setting quality
            # printing each resized image name
            print(im.filename.split('\\')[-1], " is resized")

    # ---------------------------------------------------------------------------------------------------------------
    image_folder = folderName
    print("imagefolder ", image_folder)# make sure to use your folder
    print("video folder path ", video_folder_path)# make sure to use your folder
    video_name = 'Enhanced_Video.avi'

    os.chdir(video_folder_path)

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    images.sort()
    # Array images should only consider
    # the image files ignoring others if any
    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'MP4V'), rate, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Deallocating memories taken for window creation
    # cv2.destroyAllWindows()
    # video.release()  # releasing the video generated
    print(video_folder_path.split('\\')[4])
    return video_folder_path.split('\\')[4]