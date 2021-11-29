import os


def createFolder():
    parentPath = "E:\\BACKBONE\\image_enhancement\\Frames"

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
    directory = "Frames" + str(count)

    # Parent Directory path
    parent_dir = "E:\\BACKBONE\\image_enhancement\\Frames\\"

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("Directory '% s' created" % directory)
    return directory


def createFolderForEnhancedFrames(folderName):
    print("folder name in createFolderForEnhancedFrames : " + folderName)
    parentPath = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

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
    directory = "Enhanced_Frames" + str(count)

    # Parent Directory path
    parent_dir = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("path : " + path)
    print("Directory '% s' created" % directory)
    return directory


def createFolderForContrasted(folderName):
    parentPath = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

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
    directory = "Contrast_Adjusted_Frames" + str(count)

    # Parent Directory path
    parent_dir = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("path : " + path)
    print("Directory '% s' created" % directory)
    return path


def createFolderForSharpImages(folderName):
    parentPath = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

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
    directory = "Sharp_Frames" + str(count)

    # Parent Directory path
    parent_dir = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("path : " + path)
    print("Directory '% s' created" % directory)
    return path


def DenoiseGaussian(folderName):
    parentPath = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

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
    directory = "Gaussian_Denoised_Frames" + str(count)

    # Parent Directory path
    parent_dir = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("path : " + path)
    print("Directory '% s' created" % directory)
    return path


def smoothImagesFolder(folderName):
    parentPath = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

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
    directory = "Smooth_Images" + str(count)

    # Parent Directory path
    parent_dir = "E:\\BACKBONE\\image_enhancement\\Frames\\" + folderName

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("path : " + path)
    print("Directory '% s' created" % directory)
    return path
