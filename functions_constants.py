from tkinter import * 
from PIL import ImageTk,Image
import images
import generator,options



bg_image = "images\BG.png"
button_temp_image = "images\Temp_Button.png"
pnoise_image = "images\Pnoise.PNG"
exit_image = "image\exit_image.png"
options_image = "image\options_image.png"
instructions_image = "image\instructions_image.png"
noise_image_image = "image\\noise_image_image.png"
generate_art_image = "image\generate_art_image.png"
confirm_image = "image\Confirm_image.png"
shapes_image = "image\shapes_image.png"





def make_img(filename,size="1920x1080"):
    if size=="1920x1080":
        x=Image.open(filename)
    else:
        x= Image.open(filename).resize((size))
    return ImageTk.PhotoImage(x)