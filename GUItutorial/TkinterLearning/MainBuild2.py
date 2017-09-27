'''
Created on Sep 25, 2017

@author: Kanye Southeast
'''
from Tkinter import *
import Tkinter
import os
from ttk import *
from NotebookClass import *
import ttk

master = Tk() # Declaring of main window
master.title("Superballer GUI") # Title for main window

def IPMIButtonCommand(mainframe, master): # Command to attach to IPMI button
    mainframe.destroy()
    DrawThirdScreen(master) # call up the IPMI screen
    
def BIOSButtonCommand(mainframe, master): # Command to attach to BIOS button
    mainframe.destroy()
    DrawThirdScreen(master) # call up the BIOS screen

def QuitButtonCommand(master):
    master.destroy()
    
def ReturnButtonCommand(mainframe, master): # Command to attach to return button
    mainframe.destroy()
    DrawMainScreen(master)
   
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
    
    
'''
#figuring out this tab thing

'''
n = notebook(master, LEFT) # tabs

def DrawMainScreen(master):
    mainframe = Frame(master)
    IPMI = Button(mainframe, text="IPMI Scripts", command=lambda: IPMIButtonCommand(mainframe, master))
    BIOS = Button(mainframe, text="BIOS Scripts", command=lambda: BIOSButtonCommand(mainframe, master))
    Quit = Button(mainframe, text = "Quit", command=lambda: QuitButtonCommand(master))
    IPMI.pack()
    BIOS.pack()
    Quit.pack(side=BOTTOM)
    mainframe.pack()
    
def DrawSecondScreen(master):
    mainframe = Frame(n()) # draw Frame widget as Notebook
    e1 = Entry(mainframe)
    e2 = Entry(mainframe)
    e3 = Entry(mainframe)
    e1.pack(fill=BOTH, expand=1)
    e2.pack(fill=BOTH, expand=1)
    e3.pack(fill=BOTH, expand=1)
    Label1 = Label(mainframe, text="IPMI Scripts")
    b1 = Button(mainframe, text="IPMI Script 1", command=lambda: IPMIScript1(mainframe, master))
    b2 = Button(mainframe, text="IPMI Script 2", command=lambda: IPMIScript2(mainframe, master))
    b3 = Button(mainframe, text="IPMI Script 3", command=lambda: IPMIScript3(mainframe, master))
    b4 = Button(mainframe, text="IPMI Script 4", command=lambda: IPMIScript4(mainframe, master))
    b5 = Button(mainframe, text="IPMI Script 5", command=lambda: IPMIScript5(mainframe, master))
    b6 = Button(mainframe, text="IPMI Script 6", command=lambda: IPMIScript6(mainframe, master))
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    mainframe.pack()
    b1.pack(fill=BOTH, expand=1)
    b2.pack(fill=BOTH, expand=1)
    b3.pack(fill=BOTH, expand=1)
    b4.pack(fill=BOTH, expand=1)
    b5.pack(fill=BOTH, expand=1)
    b6.pack(fill=BOTH, expand=1)
    ReturnButton.pack(side=BOTTOM)
    Label1.pack(side=TOP)
       
def DrawThirdScreen(master):
    mainframe = Frame(n()) # draw Frame widget as Notebook
    Label1 = Label(mainframe, text="BIOS Scripts")
    b1 = Button(mainframe, text="BIOS Script 1", command=lambda: BIOSScript1(mainframe, master))
    b2 = Button(mainframe, text="BIOS Script 2", command=lambda: BIOSScript2(mainframe, master))
    b3 = Button(mainframe, text="BIOS Script 3", command=lambda: BIOSScript3(mainframe, master))
    b4 = Button(mainframe, text="BIOS Script 4", command=lambda: BIOSScript4(mainframe, master))
    b5 = Button(mainframe, text="BIOS Script 5", command=lambda: BIOSScript5(mainframe, master))
    b6 = Button(mainframe, text="BIOS Script 6", command=lambda: BIOSScript6(mainframe, master))
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    mainframe.pack()
    b1.pack(fill=BOTH, expand=1)
    b2.pack(fill=BOTH, expand=1)
    b3.pack(fill=BOTH, expand=1)
    b4.pack(fill=BOTH, expand=1)
    b5.pack(fill=BOTH, expand=1)
    b6.pack(fill=BOTH, expand=1)
    ReturnButton.pack(side=BOTTOM)
    Label1.pack(side=TOP)
    
def center(win): #Centers the program window
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))
    
master.geometry('{}x{}'.format(300, 300)) #Set window size
master.resizable(width=False, height=False) #Make it so user can't resize window

from PIL import Image, ImageTk #Add Logo, automatically resize Logo
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
        size = (event.width, 100) #instead of event.height, use set height of 100
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0,0, image=self.image, anchor=NW, tags="IMG")
   
content = ttk.Frame(master)
frame = ttk.Frame(content, borderwidth=5, relief=SUNKEN, width=300, height=300)
content.grid(column=0, row=0)
#frame.grid(column=3, row=3, columnspan=6, rowspan=2)

Logo(master)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)
DrawMainScreen(master)
center(master)
master.mainloop() #The mainloop handles all the events that occur in a tkinter window, from button pressing to the commands that a button runs, very important