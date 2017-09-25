'''
Created on Sep 25, 2017

@author: dog
'''

#!/usr/bin/python

import Tkinter
import os

top=Tkinter.Tk()

def helloCallBack():
    os.system('python .\scripts\hellowhat.py')

B=Tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()