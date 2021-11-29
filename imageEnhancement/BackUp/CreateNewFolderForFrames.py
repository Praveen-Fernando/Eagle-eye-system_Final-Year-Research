# Python program to explain os.mkdir() method

# importing os module
import os

def createFolder():
    parentPath = "E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames"

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
    parent_dir = "E:\\#ProgrammingWork\\Python\\VideoEnhance\\Frames\\"

    # Path
    path = os.path.join(parent_dir, directory)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path)
    print("Directory '% s' created" % directory)
    return directory

if __name__ == '__main__':
    # Calling the function
    createFolder()

