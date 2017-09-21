'''
Created on Sep 21, 2017

@author: Isador
'''
import Tkinter
import tkMessageBox

#mass import all Tkinter stuff?
from Tkinter import *

#Big Baller in the Center position
def center(win):
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))
    
#Canvas
baller=Tk()
canvas = Canvas(baller)
canvas.pack()
baller.title("Big Baller 3.0")

from PIL import ImageTk, Image
#Logo
path = "BigBallerBrand.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = baller.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Entry Field 1 IPMI IP Address
entry1label = Label(baller, text="IPMI IP Address ")
entry1label.pack(side = LEFT)
entry1label_window = canvas.create_window(20, 10, anchor=NW, window=entry1label)
entry1entry = Entry(baller, bd = 5)
entry1entry.pack(side = RIGHT)
entry1entry_window = canvas.create_window(20, 30, anchor=NW, window=entry1entry)
print (entry1label.winfo_geometry())
print (entry1entry.winfo_geometry())

#Entry Field 2 IPMI User Name
entry2label = Label(baller, text="IPMI Username")
entry2label.pack(side = LEFT)
entry2label_window = canvas.create_window(20, 50, anchor=NW, window=entry2label)
entry2entry = Entry(baller, bd = 5)
entry2entry.pack(side = RIGHT)
entry2entry_window = canvas.create_window(20, 70, anchor=NW, window=entry2entry)
print (entry2label.winfo_geometry())
print (entry2entry.winfo_geometry())

#Entry Field 3 IPMI User Name
entry3label = Label(baller, text="IPMI Password")
entry3label.pack(side = LEFT)
entry3label_window = canvas.create_window(20, 90, anchor=NW, window=entry3label)
entry3entry = Entry(baller, bd = 5)
entry3entry.pack(side = RIGHT)
entry3entry_window = canvas.create_window(20, 110, anchor=NW, window=entry3entry)
print (entry3label.winfo_geometry())
print (entry3entry.winfo_geometry())

button1 = Button(text = "BIOS Scripts")
button1.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button1_window = canvas.create_window(20, 150, anchor=NW, window=button1)
button1.update()
print (button1.winfo_geometry())

button2 = Button(text = "IPMI Scripts")
button2.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button2_window = canvas.create_window(20, 190, anchor=NW, window=button2)
button2.update()
print (button2.winfo_geometry())

button3 = Button(text = "Other Scripts")
button3.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button3_window = canvas.create_window(20, 230, anchor=NW, window=button3)
button3.update()
print (button3.winfo_geometry())

center(baller)
baller.mainloop()