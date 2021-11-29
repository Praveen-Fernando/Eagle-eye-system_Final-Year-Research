import os

path = os.chdir("E:\\#ProgrammingWork\\pyCharm\\imageEnhancement\\a")

#c = 0;
#for fileCount in os.listdir(path):
#    c = c +1
#print(c)

i = 10000000

for file in os.listdir(path):

    new_file_name = "{}.jpg".format(i)
    os.rename(file, new_file_name)

    i = i + 1