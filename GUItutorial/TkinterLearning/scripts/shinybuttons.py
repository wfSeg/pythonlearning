'''
Created on Sep 21, 2017

@author: Long
'''
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def Abutton():
    tkMessageBox.showinfo("PopupBox","Lonzo Ball")
    
Button = Tkinter.Button(top,
                        text = "2017 1st Pick", 
                        height=1, 
                        pady = 0, 
                        width=10, 
                        padx = 3, 
                        activebackground = "#0C1EF5",#blue
                        activeforeground = "#F5F10C",#yellow
                        bg = "#0B1049",#darkpurple
                        fg = "#E8E9F4",#whitish
                        command = Abutton)
    
Button.pack()
top.mainloop()