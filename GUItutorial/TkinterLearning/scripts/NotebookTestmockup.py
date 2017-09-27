'''
Created on Sep 27, 2017

@author: Swaggy P
'''

from Tkinter import *
from NotebookClass import *
#from CenterClass import *

a = Tk()
n = notebook(a, LEFT)

# uses the notebook's frame
f1 = Frame(n())
b1 = Button(f1, text = "Button 1")
e1 = Entry(f1)
e2 = Entry(f1)
e3 = Entry(f1)
# pack your widgets before adding the frame
# to the notebook (but not the frame itself)!
b1.pack(fill=BOTH, expand=1)
e1.pack(fill=BOTH, expand=1)
e2.pack(fill=BOTH, expand=1)
e3.pack(fill=BOTH, expand=1)

f2 = Frame(n())
# this button destroys the 1st screen radiobutton
b2 = Button(f2, text='Button 2', command=lambda:x1.destroy())
b3 = Button(f2, text='Beep 2', command=lambda:Tk.bell(a))
b2.pack(fill=BOTH, expand=1)
b3.pack(fill=BOTH, expand=1)

f3 = Frame(n())

# keeps the reference to the radiobutton (optional)
x1 = n.add_screen(f1, "Screen 1")
n.add_screen(f2, "Screen 2")
n.add_screen(f3, "dummy")

if __name__ == "__main__":
    def center(win): #Centers the program window
        win.update_idletasks()
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        win.geometry("%dx%d+%d+%d" % (size + (x,y)))
    
    center(a)
    a.geometry('{}x{}'.format(300, 300)) #Set window size
    a.resizable(width=False, height=False) #Make it so user can't resize window
    a.mainloop()
    
# END