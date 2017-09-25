'''
Created on Sep 25, 2017

@author: a monkey
'''

#!/usr/bin/python
import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    os.system('python hellowhat.py')

B=Tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()