'''
Created on Sep 25, 2017

@author: Kanye Southeast
'''
from Tkinter import *
import Tkinter
import os
from ttk import *
import ttk
import tkMessageBox

master = Tk() # Declaring of main window
master.title("Superballer GUI") # Title for main window
note = Notebook(master)
   
# Put path/directory of scripts here, put .py in the /scripts folder
def BIOSScript1(mainframe, master):
    os.system('python scripts/canvashuh.py')
def BIOSScript2(mainframe, master):
    os.system('python scripts/hellowhat.py')
def BIOSScript3(mainframe, master):
    os.system('python scripts/DraftPick.py')
def BIOSScript4(mainframe, master):
    os.system('python scripts/ButtonToOpenNewMenu.py')
def BIOSScript5(mainframe, master):
    os.system('python scripts/helloworld.py')
def BIOSScript6(mainframe, master):
    os.system('python scripts/sigh.py')
def IPMIScript1(mainframe, master):
    os.system('python scripts/canvashuh.py')
def IPMIScript2(mainframe, master):
    os.system('python scripts/hellowhat.py')
def IPMIScript3(mainframe, master):
    os.system('python scripts/DraftPick.py')
def IPMIScript4(mainframe, master):
    os.system('python scripts/ButtonToOpenNewMenu.py')
def IPMIScript5(mainframe, master):
    os.system('python scripts/helloworld.py')
def IPMIScript6(mainframe, master):
    os.system('python scripts/sigh.py')    
          
def center(win): #Centers the program window
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))
    
def quit():
    tkMessageBox.showinfo("Real Talk", "Real Ballers Never Quit\nKeep Hustlin'!")
    master.destroy

# Main Window Size
master.geometry('{}x{}'.format(400, 500)) #Set window size
master.resizable(width=False, height=False) #Make it so user can't resize window

# Main Menu Tab
tab1 = Frame(note)
note.add(tab1, text="Main")
Button(tab1, text = "Quit", command=quit).pack(padx=50, pady=50)
from PIL import Image, ImageTk # Add Logo
#Added Logo
class Logo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open('.\images\BigBallerBrand.jpg')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0,0, image=self.image, anchor=NW, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)
        
    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0,0, image=self.image, anchor=NW, tags="IMG")
Logo(master)

# IPMI Tab
tab2 = Frame(note)
note.add(tab2, text="IPMI")
e1 = Entry(tab2)
e2 = Entry(tab2)
e3 = Entry(tab2)
b1 = Button(tab2, text="IPMI Script 1", command=lambda: IPMIScript1(tab2, master))
b2 = Button(tab2, text="IPMI Script 2", command=lambda: IPMIScript2(tab2, master))
b3 = Button(tab2, text="IPMI Script 3", command=lambda: IPMIScript3(tab2, master))
b4 = Button(tab2, text="IPMI Script 4", command=lambda: IPMIScript4(tab2, master))
b5 = Button(tab2, text="IPMI Script 5", command=lambda: IPMIScript5(tab2, master))
b6 = Button(tab2, text="IPMI Script 6", command=lambda: IPMIScript6(tab2, master))
Label(tab2, text="Enter IPMI IP Address").grid(row=0, column=0, padx=5, pady=5, sticky=W)
e1.grid(row=0, column=1)
Label(tab2, text="Enter Username").grid(row=1, column=0, padx=5, pady=5, sticky=W)
e2.grid(row=1, column=1)
Label(tab2, text="Enter Password").grid(row=2, column=0, padx=5, pady=5, sticky=W)
e3.grid(row=2, column=1)
Label(tab2, text="IPMI Scripts").grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky=W)
b1.grid(row=5, column=0, padx=5, pady=5, sticky=W)
b2.grid(row=5, column=1, padx=5, pady=5, sticky=W)
b3.grid(row=5, column=2, padx=5, pady=5, sticky=W)
b4.grid(row=6, column=0, padx=5, pady=5, sticky=W)
b5.grid(row=6, column=1, padx=5, pady=5, sticky=W)
b6.grid(row=6, column=2, padx=5, pady=5, sticky=W)

# BIOS Tab
tab3 = Frame(note)
note.add(tab3, text="BIOS")
Label1 = Label(tab3, text="BIOS Scripts")
b1 = Button(tab3, text="BIOS Script 1", command=lambda: BIOSScript1(tab3, master))
b2 = Button(tab3, text="BIOS Script 2", command=lambda: BIOSScript2(tab3, master))
b3 = Button(tab3, text="BIOS Script 3", command=lambda: BIOSScript3(tab3, master))
b4 = Button(tab3, text="BIOS Script 4", command=lambda: BIOSScript4(tab3, master))
b5 = Button(tab3, text="BIOS Script 5", command=lambda: BIOSScript5(tab3, master))
b6 = Button(tab3, text="BIOS Script 6", command=lambda: BIOSScript6(tab3, master))
Label(tab3, text="BIOS Scripts").grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky=W)
b1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
b2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
b3.grid(row=1, column=2, padx=5, pady=5, sticky=W)
b4.grid(row=2, column=0, padx=5, pady=5, sticky=W)
b5.grid(row=2, column=1, padx=5, pady=5, sticky=W)
b6.grid(row=2, column=2, padx=5, pady=5, sticky=W)

# Misc. Tab
tab4 = Frame(note)
note.add(tab4, text="Misc.")
   
note.pack()
center(master)
master.mainloop() #The mainloop handles all the events that occur in a tkinter window, from button pressing to the commands that a button runs, very important
