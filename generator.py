from tkinter import * 
from PIL import ImageTk,Image
import images
import options,common_functions



def generator_1():
    gen_1= Toplevel()
    gen_1.title("Generator")
    gen_1.geometry("1920x1080")

    gen_background = common_functions.make_img("images\Temp_BG.png",)

    gen_canvas = Canvas(gen_1)
    gen_canvas.pack(fill="both",expand=True)

    gen_canvas.create_image(0,0,image=gen_background,anchor="nw")

    gen_canvas.create_text(400,250,text="Choose Your desired Moden Art Type:",font=("",28),fill="White")


    Pnoise_image = common_functions.make_img("images\Pnoise.PNG",(100,50))



    Pnoise_button = Button(gen_1,image=Pnoise_image)


    Pnoise_button_window = gen_canvas.create_window(50,400,anchor="nw",window=Pnoise_button)




    mainloop()










