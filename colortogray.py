
from PIL import Image,ImageTk, ImageOps 

path='/storage/emulated/0/Pythonimage/Newpy/'

yourpic = 'Pic.jpg'

gray=yourpic.split('.')
name_to_save_grayimg = gray[0]+'grayscale.'+gray[1]

def convert(data):
	img = Image.open(data)
	grayimg = ImageOps.grayscale(img)
	grayimg.save(name_to_save_grayimg)

convert(path+yourpic)
	
from tkinter import *

root = Tk() 

w=root.winfo_screenwidth()
h=root.winfo_screenheight()

root.overrideredirect(True)
root.geometry(str(w)+"x"+str(h)+"+0+0")
root.config(bg='white')

img1 = ImageTk.PhotoImage(file=path+yourpic)

label1=Label(root, image=img1)
label1.place( x=80,y=350)

img2 = ImageTk.PhotoImage(file=path+name_to_save_grayimg)

label2=Label(root, image=img2)
label2.place(x=80, y=1100)

label3=Label(root, text=' Colourful to Grayscale ', bg='yellow',fg='red',font="times 12 bold")
label3.place(x=100, y=50)

label4=Label(root, text=' Your Picture ', bg='white',fg='blue',font="times 10 bold")
label4.place(x=300, y=250)

label5=Label(root, text=' Grayscale Picture ', bg='white',fg='blue',font="times 10 bold")
label5.place(x=250, y=1000)

root.mainloop()
