from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import PIL.Image
import PIL.ImageTk

def choose():
    folder_selected = filedialog.askdirectory()
    labelVar.set(folder_selected)
    Button(can,text="create", command= lambda: createFiles(folder_selected), height=1, width=15, bd=1).place(x=140,y=100)

def createFiles(src):
    html = open(src + "\index.html", "w")
    html.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n\t<meta charset='UTF-8'>\n\t<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\t<title>Document</title>\n\t<link rel='stylesheet' href='style.css'>\n\t<script src='main.js' defer></script>\n</head>\n<body>\n</body>\n</html>")
    html.close()

    css = open(src + "\style.css", "w")
    css.write("*{\n\tmargin: 0%;\n\tpadding: 0%;\n\tbox-sizing: border-box;\n\tfont-family: monospace;\n}")
    css.close()

    js = open(src + "\main.js", "w")
    js.write("//have fun coding")
    js.close()

root=Tk()
root.title("Html Generator")
root.iconbitmap('coffee.ico')
root.geometry("300x200")
can = Canvas(root, width=300,height=200)
can.place(relx=0.5, rely=0.5, anchor=CENTER)

global entry

labelVar = StringVar()
Label(can, text="Html Project Generator",font=("Arial", 15)).place(x=30,y=30)
dirs = Label(can, text="Selected Folder", textvariable=labelVar).place(x=30,y=70)

Button(can,text="Choose Folder", command=choose, height=1, width=15, bd=1).place(x=30,y=100)

# Read the Image
image = PIL.Image.open("coffee.png")
 
# Resize the image using resize() method
resize_image = image.resize((100, 100))
 
img = PIL.ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
Label(can,image=img).place(relx=0.8, rely=0.7, anchor=CENTER)

root.mainloop()




