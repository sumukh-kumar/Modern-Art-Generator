from tkinter import * 
from PIL import ImageTk,Image
import images
import generator,options



def make_img(filename,size="1920x1080"):
    if size=="1920x1080":
        x=Image.open(filename)
    else:
        x= Image.open(filename).resize((size))
    return ImageTk.PhotoImage(x)