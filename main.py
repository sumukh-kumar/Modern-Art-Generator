from tkinter import * 
from PIL import ImageTk,Image
import images
import generator,options,common_functions



root = Tk()
root.title("Modern Art Generator")
root.geometry("1920x1080")



Background_Image = common_functions.make_img("images\Temp_BG.png",)

Gen_button_image = common_functions.make_img("images\Temp_Button.png",(100,50))



root_canvas = Canvas(root)
root_canvas.pack(fill="both",expand=True)

root_canvas.create_image(0,0,image=Background_Image,anchor="nw")

root_canvas.create_text(400,250,text="Modern Art Generator",font=("",28),fill="White")


Gen_button = Button(root,text="Start",image=Gen_button_image,command=generator.generator_1)
Options_button = Button(root,text="Options")
Exit_button = Button(root,text="Exit",command=root.destroy)


Gen_button_window = root_canvas.create_window(50,400,anchor="nw",window=Gen_button)
Options_button_window = root_canvas.create_window(50,550,anchor="nw",window=Options_button)
Exit_button_window = root_canvas.create_window(50,700,anchor="nw",window=Exit_button)




mainloop()