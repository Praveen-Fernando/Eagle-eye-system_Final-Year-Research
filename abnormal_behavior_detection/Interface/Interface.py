# Import Module
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

class eye:

    def __init__(self ,master):
        frame = Frame(master)   # Top frame
        frame.pack()
        tkinter.Button(frame, text="UPLOAD VIDEO", bg="#018934", fg="white", font=("Arial", 10, "bold"), width=30,
                     height=2,command=self.main).pack(side="right")


    def main(self):

        os.system('python ../HumanDetection/Human_Detection_Video.py')
        #os.system('python ../HumanDetection/Human_Detection_Image.py')
        os.system('python ../FramesConverter/Frames_To_Video.py')
        #os.system('python ../FramesConverter/Frames_To_Video_Test.py')
        os.system('python ../WeaponDetection/Weapon_Detection.py')


#Quit Window
def quit(root):
    root.destroy()

#Create Tkinter Object
root = Tk()
root.geometry("1000x500")
root.configure(background="white")

#Title
label2 = Label(root,
               text="Abnormal Behavior Detection",
               fg = "dark green",
               bg = "white",
               font = "Helvetica 24 bold").pack()

#Read the Image
image = Image.open("5.png")

#Reszie the image using resize() method
resize_image = image.resize((300, 300))

img = ImageTk.PhotoImage(resize_image)


#create label and add resize Logo image
label1 = Label(image=img, bg = "white")
label1.image = img
label1.pack()


button2 = Button(root, text="EXIT", bg="#DB4D39", command=lambda root=root :quit(root), fg="white", font=("Arial", 10, "bold"), width=30, height=2)
#button2.pack(side = LEFT, padx=20, pady=40)
button2.place(x=375, y=410)

obj  = eye(root)

root.mainloop()