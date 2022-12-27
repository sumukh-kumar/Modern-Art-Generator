from tkinter import * 
from PIL import ImageTk,Image
import images
import generator,options

root = Tk()
root.title("Modern Art Generator")
root.geometry("1920x1080")




bg= PhotoImage(file="images\Temp_BG.png")


my_canvas = Canvas(root)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0,image=bg,anchor="nw")

my_canvas.create_text(400,250,text="Modern Art Generator",font=("",28),fill="White")


button1= Button(root,text="Start",command=generator.count)
button2= Button(root,text="Options")
button3= Button(root,text="Exit")


button1_window = my_canvas.create_window(50,400,anchor="nw",window=button1)
button2_window = my_canvas.create_window(50,550,anchor="nw",window=button2)
button3_window = my_canvas.create_window(50,700,anchor="nw",window=button3)










""" 
my_label = Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

fake_text = Label(root,text="")
button1= Button(root,text="Generate Art")
button2= Button(root,text="Options")
button3= Button(root,text="Exit")

fake_text.grid(row=0,column=0,padx=20,pady=100)
button1.grid(row=1,column=0,padx=20,pady=50)
button2.grid(row=2,column=0,padx=20,pady=50)
button3.grid(row=3,column=0,padx=20,pady=50) """


root.mainloop()