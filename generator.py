from tkinter import * 
from PIL import ImageTk,Image
import images



def generator_1():
    gen_1= Toplevel()
    gen_1.title("Generator")
    gen_1.geometry("1920x1080")

    gen_bg = Image.open("images\Temp_BG.png")
    gen_refined = ImageTk.PhotoImage(gen_bg)

    gen_canvas = Canvas(gen_1)
    gen_canvas.pack(fill="both",expand=True)

    gen_canvas.create_image(0,0,image=gen_refined,anchor="nw")


    mainloop()










