from tkinter import * 
from PIL import ImageTk,Image
import images
import turtle
import generator,options,functions_constants,rectangle_code


root = Toplevel()
root.title("Modern Art Generator")
root.geometry("1920x1080")


Background_Image = functions_constants.make_img(functions_constants.bg_image,(1920,1080))
Gen_button_image = functions_constants.make_img(functions_constants.generate_art_image,(200,100))
Instructions_image = functions_constants.make_img(functions_constants.instructions_image,(200,100))
Exit_image = functions_constants.make_img(functions_constants.exit_image,(200,100))

Modern_title_image = functions_constants.make_img(functions_constants.modern_title,(1000,500))
Credits_image = functions_constants.make_img(functions_constants.credits_image,(500,300))


root_canvas = Canvas(root)
root_canvas.pack(fill="both",expand=True)

root_canvas.create_image(0,0,image=Background_Image,anchor="nw")
root_canvas.create_image(450,100,image=Modern_title_image,anchor="nw")
root_canvas.create_image(1400,750,image=Credits_image,anchor="nw")


Gen_button = Button(root,image=Gen_button_image,command=generator.generator_1)
Options_button = Button(root,image=Instructions_image,command=options.options_clicked)
Exit_button = Button(root,image=Exit_image,command=turtle.bye)


Gen_button_window = root_canvas.create_window(50,400,anchor="nw",window=Gen_button)
Options_button_window = root_canvas.create_window(50,575,anchor="nw",window=Options_button)
Exit_button_window = root_canvas.create_window(50,750,anchor="nw",window=Exit_button)




mainloop()