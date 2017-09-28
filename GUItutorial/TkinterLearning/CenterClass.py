'''
Created on Sep 27, 2017

@author: uhuhuh
'''

# Is this how "Class" work???
# Centers the program window
from Tkinter import *

class center: 
    #init and receives master widget
    
    def __init__(self, master=None):
        
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.geometry("%dx%d+%d+%d" % (size + (x,y)))