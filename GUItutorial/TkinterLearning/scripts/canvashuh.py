'''
Created on Sep 21, 2017

@author: Yeezy
'''

import Tkinter
import tkMessageBox

#centering the damn popup window. It worked!
def center(win):
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))


#the canvas
top = Tkinter.Tk()

C = Tkinter.Canvas(top, 
                   bg="blue",
                   height=250,
                   width=300,
                   )

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

center(top)
C.pack()
top.mainloop()


    