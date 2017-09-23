'''
Created on Sep 21, 2017

@author: Isador
'''
#!/usr/bin/python
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
baller = Tk() #main window, usually called "master" or "root", I call it "baller"
canvas = Canvas(baller)
canvas.pack(fill=BOTH, expand=YES)
baller.title("Big Baller 3.0")

#Logo
from PIL import ImageTk, Image
#Logo
path = "S:\images\BigBallerBrand.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Tkinter.Label(baller, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


#Entry Field 1 IPMI IP Address
entry1label = Label(baller, text="IPMI IP Address ")
entry1label.pack(side = LEFT)
entry1label_window = canvas.create_window(0, 20, anchor=NW, window=entry1label)
entry1entry = Entry(baller, bd = 5)
entry1entry.pack(side = RIGHT)
entry1entry.focus_set()
entry1entry_window = canvas.create_window(120, 20, anchor=NW, window=entry1entry)
print (entry1label.winfo_geometry())
print (entry1entry.winfo_geometry())

""" need figure out Entry
def e1():
    print entry1entry.get()
#Entry 1 button check
e1b = Button(text = "check", command = e1)
e1b.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
e1b_window = canvas.create_window(100, 20, anchor=NW, window=e1b)
e1b.update()
print (e1b.winfo_geometry())
"""

#Entry Field 2 IPMI User Name
entry2label = Label(baller, text="IPMI Username")
entry2label.pack(side = LEFT)
entry2label_window = canvas.create_window(0, 60, anchor=NW, window=entry2label)
entry2entry = Entry(baller, bd = 5)
entry2entry.pack(side = RIGHT)
entry2entry_window = canvas.create_window(120, 60, anchor=NW, window=entry2entry)
print (entry2label.winfo_geometry())
print (entry2entry.winfo_geometry())

#Entry Field 3 IPMI User Name
entry3label = Label(baller, text="IPMI Password")
entry3label.pack(side = LEFT)
entry3label_window = canvas.create_window(0, 100, anchor=NW, window=entry3label)
entry3entry = Entry(baller, bd = 5)
entry3entry.pack(side = RIGHT)
entry3entry_window = canvas.create_window(120, 100, anchor=NW, window=entry3entry)
print (entry3label.winfo_geometry())
print (entry3entry.winfo_geometry())

#Functions
#placeholder
def Placeholder():
    tkMessageBox.showinfo("Ballin'", "Sorry, We're All Sold Out!\nCheck back again later")

def b1():
    import BIOSScripts
def b2():
    top = Toplevel()
def b3():
    top = Toplevel()
#Buttons
#BIOS Button
button1 = Button(text = "BIOS Scripts", command = b1)
button1.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button1_window = canvas.create_window(0, 140, anchor=NW, window=button1)
button1.update()
print (button1.winfo_geometry())

#IPMI Button
button2 = Button(text = "IPMI Scripts", command = b2)
button2.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button2_window = canvas.create_window(80, 140, anchor=NW, window=button2)
button2.update()
print (button2.winfo_geometry())

#Other Button
button3 = Button(text = "Other Scripts", command = b3)
button3.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button3_window = canvas.create_window(160, 140, anchor=NW, window=button3)
button3.update()
print (button3.winfo_geometry())

#Baller Button
button4 = Button(text = "Order ZO2 Prime Remix", command = Placeholder)
button4.configure(width = 0,
                  activebackground = "Yellow",
                  relief = GROOVE)
button4_window = canvas.create_window(0, 180, anchor=NW, window=button4)
button4.update()
print (button3.winfo_geometry())


center(baller)
baller.mainloop()