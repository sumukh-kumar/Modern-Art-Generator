from tkinter import * 
from PIL import ImageTk,Image
import images
import turtle
import generator,options,functions_constants,rectangle_code


def options_clicked():
    option = Toplevel()
    option.title("Instructions")
    option.geometry("1920x1080")


    ibg = functions_constants.make_img(functions_constants.instructions_bg,(1920,1080))

    option_canvas = Canvas(option)
    option_canvas.pack(fill="both",expand=True)


    option_canvas.create_image(0,0,image=ibg,anchor="nw")

    mainloop()


























































































