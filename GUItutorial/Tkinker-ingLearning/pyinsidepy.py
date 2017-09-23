'''
Created on Sep 22, 2017

@author: Ye
'''

#!/usr/bin/python

import Tkinter
import tkMessageBox
#from PIL import ImageTk, Image
#from Tkinter import *
import os

top = Tkinter.Tk()

#keep getting error "0x000034ec (most recent call first):"
def DoSomething():
    #import hellowhat
      os.system('BigBallin.py')
    
B = Tkinter.Button(top, text = "Launch", command = DoSomething)

B.pack()
top.mainloop()