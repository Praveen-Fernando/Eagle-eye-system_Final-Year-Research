# from tkinter import filedialog
# import shutil
# from face_detection import *
# from face_detection_recognition import *
# from csv_handler import *
# import os
#
#
# # Important part
# def selectMultiImage(opt_menu, menu_var):
#     global img_list, current_slide, slide_caption, slide_control_panel
#
#     filetype = [("images", "*.jpg *.jpeg *.png")]
#     # pass images to here
#     path_list = filedialog.askopenfilenames(title="Choose atleast 10 images", filetypes=filetype)
#
#     if (len(path_list) < 5):
#         print("Error", "Choose atleast 10 images.")
#     else:
#         img_list = []
#         current_slide = -1
#
#         # Resetting slide control panel
#         if (slide_control_panel != None):
#             slide_control_panel.destroy()
#
#         # Creating Image list
#         for path in path_list:
#             img_list.append(cv2.imread("path"))  # path reader
#
#         # Creating slideshow of images
#         current_slide += 1
#
#
# # Important part
# def register(entries, required, menu_var):
#     global img_list
#
#     # Fetching data from entries
#     entry_data = {}
#     for i, entry in enumerate(entries):
#         # print(i)
#         val = entry[1].get()
#         # print(val)
#
#         if (len(val) == 0 and required[i] == 1):
#             return
#         else:
#             entry_data[entry[0]] = val.lower()
#
#     # Setting Directory
#     path = os.path.join('Criminals', "1")
#     if not os.path.isdir(path):
#         os.mkdir(path)
#
#     no_face = []
#     for i, img in enumerate(img_list):
#         # Storing Images in directory
#         id = registerCriminal(img, path, i + 1)
#         if (id != None):
#             no_face.append(id)
#
#     # check if any image doesn't contain face
#     if (len(no_face) > 0):
#         no_face_st = ""
#         for i in no_face:
#             no_face_st += "Image " + str(i) + ", "
#         print("Registration Error", "Registration failed!\n\nFollowing images doesn't contain"
#                                     " face or Face is too small:\n\n%s" % (no_face_st))
#         shutil.rmtree(path, ignore_errors=True)
#     else:
#         # Storing data in database
#         insertData(entry_data)
#         rowId = 1
#         if (rowId >= 0):
#             print("Success", "Criminal Registered Successfully.")
#             shutil.move(path, os.path.join('Criminals', entry_data["Name"]))
#
#         else:
#             shutil.rmtree(path, ignore_errors=True)
#             print("Database Error", "Some error occured while storing data.")
