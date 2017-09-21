'''
Created on Sep 21, 2017

@author: Isador
'''
import Tkinter
import tkMessageBox

#mass import all Tkinter stuff?
from Tkinter import *

#centering the window
def center(win):
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))
    
#Canvas
root=Tk()
canvas = Canvas(root)
canvas.pack()

#figure out how to put Entry instead of buttons...
"""
entry1label = Label(root, text="IPMI IP Address ")
entry1label.pack(side = LEFT)
entry1entry = Entry(root, bd = 5)
entry1entry.pack(side = RIGHT)"""


button1 = Button(text = "IPMI IP Address")
button1.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button1_window = canvas.create_window(20, 10, anchor=NW, window=button1)
button1.update()
print (button1.winfo_geometry())

button2 = Button(text = "Username and Password")
button2.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button2_window = canvas.create_window(20, 50, anchor=NW, window=button2)
button2.update()
print (button2.winfo_geometry())

button3 = Button(text = "BIOS Scripts")
button3.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button3_window = canvas.create_window(20, 90, anchor=NW, window=button3)
button3.update()
print (button3.winfo_geometry())

center(root)
root.mainloop()