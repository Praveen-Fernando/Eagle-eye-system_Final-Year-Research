import os

path = "/imageEnhancement\\Frames"

totalFiles = 0

totalDir = 0

for base, dirs, files in os.walk(path):
    print('Searching in : ', base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1

# print('Total number of files', totalFiles)
print('Total Number of directories', totalDir)
# print('Total:', (totalDir + totalFiles))



