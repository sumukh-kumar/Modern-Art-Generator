from tkinter import * 
from PIL import ImageTk,Image
import images
import generator,options



bg_image = "images/BG.png"
button_temp_image = "images/Temp_Button.png"
pnoise_image = "images/Pnoise.PNG"
exit_image = "images/exit_image.png"
options_image = "images/options_image.png"
instructions_image = "images/instructions_image.png"
noise_image_image = "images/noise_image_image.png"
generate_art_image = "images/generate_art_image.png"
confirm_image = "images/Confirm_image.png"
shapes_image = "images/shapes_image.png"
instructions_bg = "images/optionsmenu.png"

modern_title = "images/Modern_title.png"
please_colour_title = "images/please_colour_title.png"
credits_image = "images/credits.png"
choose_art_title = "images/Choose_art_title.png"
choose_colour_title = "images/Choose_colour_title.png"




def make_img(filename,size="1920x1080"):
    if size=="1920x1080":
        x=Image.open(filename)
    else:
        x= Image.open(filename).resize((size))
    return ImageTk.PhotoImage(x)