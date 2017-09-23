'''
Created on Sep 22, 2017

@author: Yuh
'''
#!/usr/bin/python
import Tkinter
import tkMessageBox
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
lonzo = Tk() #main window, Lonzo.
canvas = Canvas(lonzo)
canvas.pack(fill=BOTH, expand=YES)
lonzo.title("Playmaking Plays")
"""
#Logo
from PIL import ImageTk, Image
#Logo
path = "S:\images\BigBallerBrand.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Tkinter.Label(lonzo, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
"""
#Functions
def b1():
    top = Toplevel()
def b2():
    top = Toplevel()
def b3():
    top = Toplevel()
def b4():
    top = Toplevel()
    
#Buttons
#Button 1
button1 = Button(text = "Script 1", padx = 10, pady = 5, command = b1)
button1.configure(width = 0, activebackground = "Yellow", relief = GROOVE)
button1_window = canvas.create_window(0, 10, anchor=NW, window=button1)
button1.update()
print (button1.winfo_geometry())
b1label = Label(lonzo, text="Short Description: This script does this", padx = 10, pady = 5)
b1label.pack(side = RIGHT)
b1label_window = canvas.create_window(150, 10, anchor=NW, window=b1label)
print (b1label.winfo_geometry())

#Button 2
button2 = Button(text = "Script 2", padx = 10, pady = 5, command = b2)
button2.configure(width = 0, activebackground = "Yellow", relief = GROOVE)
button2_window = canvas.create_window(0, 50, anchor=NW, window=button2)
button2.update()
print (button2.winfo_geometry())
b2label = Label(lonzo, text="Short Description: This script does this", padx = 10, pady = 5)
b2label.pack(side = RIGHT)
b2label_window = canvas.create_window(150, 50, anchor=NW, window=b2label)
print (b2label.winfo_geometry())

#Button 3
button3 = Button(text = "Script 3", padx = 10, pady = 5, command = b3)
button3.configure(width = 0, activebackground = "Yellow", relief = GROOVE)
button3_window = canvas.create_window(0, 90, anchor=NW, window=button3)
button3.update()
print (button3.winfo_geometry())
b3label = Label(lonzo, text="Short Description: This script does this", padx = 10, pady = 5)
b3label.pack(side = RIGHT)
b3label_window = canvas.create_window(150, 90, anchor=NW, window=b3label)
print (b3label.winfo_geometry())

#Button 4
button4 = Button(text = "Script 4", padx = 10, pady = 5, command = b4)
button4.configure(width = 0, activebackground = "Yellow", relief = GROOVE)
button4_window = canvas.create_window(0, 130, anchor=NW, window=button4)
button4.update()
print (button4.winfo_geometry())
b4label = Label(lonzo, text="Short Description: This script does this", padx = 10, pady = 5)
b4label.pack(side = RIGHT)
b4label_window = canvas.create_window(150, 130, anchor=NW, window=b4label)
print (b4label.winfo_geometry())

center(lonzo)
lonzo.mainloop()