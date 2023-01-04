from tkinter import * 
from PIL import ImageTk,Image
import images
import generator,options



bg_image = "images\BG.png"
button_temp_image = "images\Temp_Button.png"
pnoise_image = "images\Pnoise.PNG"






def make_img(filename,size="1920x1080"):
    if size=="1920x1080":
        x=Image.open(filename)
    else:
        x= Image.open(filename).resize((size))
    return ImageTk.PhotoImage(x)