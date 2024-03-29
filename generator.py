from tkinter import * 
from PIL import ImageTk,Image
import images
import options,functions_constants,noise_functions,rectangle_code




def pnoise_clicked():


    def pconfirm_clicked():
        color_chosen=clicked.get()
        if color_chosen=="Choose Desired Color":
            pgen_canvas.create_image(450,600,image=pgen_title2,anchor="nw")
        else:
            noise_functions.pnoise(color_chosen)

    pgen = Toplevel()
    pgen.title("Generator")
    pgen.geometry("1920x1080")

    pgen_background = functions_constants.make_img(functions_constants.bg_image,(1920,1080))
    pgen_title = functions_constants.make_img(functions_constants.choose_colour_title,(1000,500))
    pgen_title2 = functions_constants.make_img(functions_constants.please_colour_title,(1000,500))

    pgen_canvas = Canvas(pgen)
    pgen_canvas.pack(fill="both",expand=True)

    pgen_canvas.create_image(0,0,image=pgen_background,anchor="nw")
    pgen_canvas.create_image(450,100,image=pgen_title,anchor="nw")

    pn_confirm_img = functions_constants.make_img(functions_constants.confirm_image,(200,100))

    pn_confirm_button = Button(pgen,image=pn_confirm_img,command=pconfirm_clicked)

    pn_confirm_window = pgen_canvas.create_window(50,700,anchor="nw",window=pn_confirm_button)


    clicked= StringVar()
    clicked.set("Choose Desired Color")

    colors = [
        "gray",
        "spring",
        "autumn",
        "winter",
        "hot",
        "copper"
    ]

    color_dropdown = OptionMenu(pgen,clicked, *colors)

    color_dropdown_window = pgen_canvas.create_window(50,500,anchor="nw",window=color_dropdown)

    mainloop()


def rec_clicked():
    rectangle_code.generate()


def generator_1():
    gen_1= Toplevel()
    gen_1.title("Generator")
    gen_1.geometry("1920x1080")

    gen_background = functions_constants.make_img(functions_constants.bg_image,(1920,1080))
    gen_title = functions_constants.make_img(functions_constants.choose_art_title,(1000,500))

    gen_canvas = Canvas(gen_1)
    gen_canvas.pack(fill="both",expand=True)

    gen_canvas.create_image(0,0,image=gen_background,anchor="nw")
    gen_canvas.create_image(450,100,image=gen_title,anchor="nw")



    Pnoise_image = functions_constants.make_img(functions_constants.noise_image_image,(200,100))
    Rec_image = functions_constants.make_img(functions_constants.shapes_image,(200,100))


    Pnoise_button = Button(gen_1,image=Pnoise_image,command=pnoise_clicked)
    Rec_button = Button(gen_1,image=Rec_image,command=rec_clicked)


    Pnoise_button_window = gen_canvas.create_window(50,400,anchor="nw",window=Pnoise_button)
    Rec_button_window = gen_canvas.create_window(50,575,anchor="nw",window=Rec_button)



    mainloop()










