'''
Created on Sep 21, 2017

@author: Long
'''
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def B1Popup():
    tkMessageBox.showinfo("PopupBox","Lonzo Ball")
def B2Popup():
    tkMessageBox.showinfo("PopupBox","Markelle Fultz")
    
Button1 = Tkinter.Button(top,
                        text = "2017 1st Pick", 
                        height=1, 
                        pady = 0, 
                        width=10, 
                        padx = 3, 
                        activebackground = "#0C1EF5",#blue
                        activeforeground = "#F5F10C",#yellow
                        bg = "#0B1049",#darkpurple
                        fg = "#E8E9F4",#whitish
                        command = B1Popup)
Button2 = Tkinter.Button(top,
                        text = "2017 2nd Pick", 
                        height=1, 
                        pady = 0, 
                        width=10, 
                        padx = 3, 
                        activebackground = "#0C1EF5",#blue
                        activeforeground = "#F5F10C",#yellow
                        bg = "#0B1049",#darkpurple
                        fg = "#E8E9F4",#whitish
                        command = B2Popup)

def center(win): #center the program window
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))
     
center(top)
Button1.pack()
Button2.pack()
top.mainloop()