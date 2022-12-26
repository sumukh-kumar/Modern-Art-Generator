from tkinter import * 
from PIL import ImageTk,Image
import images

root = Tk()
root.title("Modern Art Generator")
root.geometry("1280x720")



bg= PhotoImage(file="images\Blank_BG.png")


#my_canvas = Canvas(root,width=800,height=500)




my_label = Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

fake_text = Label(root,text="")
button1= Button(root,text="Generate Art")
button2= Button(root,text="Options")
button3= Button(root,text="Exit")

fake_text.grid(row=0,column=0,padx=20,pady=100)
button1.grid(row=1,column=0,padx=20,pady=50)
button2.grid(row=2,column=0,padx=20,pady=50)
button3.grid(row=3,column=0,padx=20,pady=50)


root.mainloop()