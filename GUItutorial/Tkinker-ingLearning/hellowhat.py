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

B.pack()
top.mainloop()
