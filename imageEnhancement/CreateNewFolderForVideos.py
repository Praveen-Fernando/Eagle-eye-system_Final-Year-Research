import os


def createFolderForEnhancedVideos():
    parentPath = "E:\\BACKBONE\\image_enhancement\\EnhancedVideos"

    totalFiles = 0
    totalDir = 0

    for base, dirs, files in os.walk(parentPath):
        print('Searching in : ', base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1

    print('Total Number of directories', totalDir)

    count = totalDir + 1

    # Directory
    directory = "EnhancedVideo" + str(count)

    # Path
    path = os.path.join(parentPath, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("path : " + path)
    print("Directory '% s' created" % directory)
    return path
