'''
Created on Oct 6, 2017

@author: Yahoop
'''
from Tkinter import *
import Tkinter
import tkMessageBox

root=Tk()
''''dont need this part
menubar = Menu(root)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")

editmenu.add_separator()

editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)
'''

Label(root, text="Input").grid(row=0, column=0, padx=5, pady=5, sticky=W)
E1 = Entry(root,bd=5)
E1.grid(row=0, column=1)
Label(root, text="Output").grid(row=1, column=0, padx=5, pady=5, sticky=W)
def replacingletter():
    a = E1.get().replace("k", "m").replace("o", "q").replace("e", "g")
    tkMessageBox.showinfo("Output Box", a)
B1 = Tkinter.Button(text="Replace", command=replacingletter).grid(row=1, column=1, padx=5, pady=5, sticky=W)

def caesarcipher():
    translated = ''
    a = E1.get()
    for symbol in a:
        if symbol.isalpha():
            num = ord(symbol)
            num += 2
            
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            translated += chr(num)
        else:
            translated += symbol
    tkMessageBox.showinfo("Decoded", translated)
B2 = Tkinter.Button(text="Decipher", command=caesarcipher).grid(row=1, column=2, padx=5, pady=5, sticky=W)

def filtering():
    a = E1.get().translate(None, '!@#$%^&*(){}[]_+-=')
    tkMessageBox.showinfo("Output Box", a)
B3 = Tkinter.Button(text="Filter", command=filtering).grid(row=3, column=1, padx=5, pady=5, sticky=W)


def center(self):
    self.update_idletasks()
    w = self.winfo_screenwidth()
    h = self.winfo_screenheight()
    size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    self.geometry("%dx%d+%d+%d" % (size + (x,y)))

#root.config(menu=menubar)
center(root)
root.mainloop()