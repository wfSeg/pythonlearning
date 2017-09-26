'''
Created on Sep 25, 2017

@author: Ryan Gosling
'''

from Tkinter import *
from ttk import *
#from PIL import Image, ImageTk

root = Tk()
#scheduledimage=PhotoImage(Image.open('..\images\BigBallerBrand.jpg'))
note = Notebook(root)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
Button(tab1, text='Exit', command=root.destroy).pack(padx=100, pady=100)

note.add(tab1, text = "Tab One") #,image=scheduledimage, compound=TOP)
note.add(tab2, text = "Tab Two")
note.add(tab3, text = "Tab Three")
note.pack()
root.mainloop()
exit()