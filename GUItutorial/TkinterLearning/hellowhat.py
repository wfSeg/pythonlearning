'''
Created on Sep 21, 2017

@author: Long
'''
#!/usr/bin/python

import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    tkMessageBox.showinfo("Hello Button", "This is the hello message")
    
B = Tkinter.Button(top, text = "clicky", command = helloCallBack)

def center(win): #Centers the program window
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))
    
center(top)
B.pack()
top.mainloop()
