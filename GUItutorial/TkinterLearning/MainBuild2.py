'''
Created on Sep 25, 2017

@author: Kanye Southeast
'''
from Tkinter import *
import Tkinter
import os
from ttk import *
import ttk

master = Tk() # Declaring of main window
master.title("Superballer GUI") # Title for main window

def IPMIButtonCommand(mainframe, master): # Command to attach to IPMI button
    mainframe.destroy()
    DrawIPMIScreen(master) # call up the IPMI screen
    
def BIOSButtonCommand(mainframe, master): # Command to attach to BIOS button
    mainframe.destroy()
    DrawBIOSScreen(master) # call up the BIOS screen

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

from PIL import Image, ImageTk #Add Logo, automatically resize Logo

def DrawMainScreen(master):
    mainframe = Frame(master)
    IPMI = Button(mainframe, text="IPMI Scripts", command=lambda: IPMIButtonCommand(mainframe, master))
    BIOS = Button(mainframe, text="BIOS Scripts", command=lambda: BIOSButtonCommand(mainframe, master))
    Quit = Button(mainframe, text = "Quit", command=lambda: QuitButtonCommand(master))
    IPMI.grid(row=0, column=0)
    BIOS.grid(row=0, column=1)
    Quit.grid(row=1, column=0, columnspan=2)
    mainframe.pack()
    
    
def DrawIPMIScreen(master):
    mainframe = Frame() # draw Frame widget as Notebook
    e1 = Entry(mainframe)
    e2 = Entry(mainframe)
    e3 = Entry(mainframe)
    b1 = Button(mainframe, text="IPMI Script 1", command=lambda: IPMIScript1(mainframe, master))
    b2 = Button(mainframe, text="IPMI Script 2", command=lambda: IPMIScript2(mainframe, master))
    b3 = Button(mainframe, text="IPMI Script 3", command=lambda: IPMIScript3(mainframe, master))
    b4 = Button(mainframe, text="IPMI Script 4", command=lambda: IPMIScript4(mainframe, master))
    b5 = Button(mainframe, text="IPMI Script 5", command=lambda: IPMIScript5(mainframe, master))
    b6 = Button(mainframe, text="IPMI Script 6", command=lambda: IPMIScript6(mainframe, master))
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    Label(mainframe, text="Enter IPMI IP Address").grid(row=0, column=0, padx=5, pady=5, sticky=W)
    e1.grid(row=0, column=1)
    Label(mainframe, text="Enter Username").grid(row=1, column=0, padx=5, pady=5, sticky=W)
    e2.grid(row=1, column=1)
    Label(mainframe, text="Enter Password").grid(row=2, column=0, padx=5, pady=5, sticky=W)
    e3.grid(row=2, column=1)
    Label(mainframe, text="IPMI Scripts").grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky=W)
    b1.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    b2.grid(row=5, column=1, padx=5, pady=5, sticky=W)
    b3.grid(row=5, column=2, padx=5, pady=5, sticky=W)
    b4.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    b5.grid(row=6, column=1, padx=5, pady=5, sticky=W)
    b6.grid(row=6, column=2, padx=5, pady=5, sticky=W)
    ReturnButton.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky=W)
    mainframe.pack()
           
def DrawBIOSScreen(master):
    mainframe = Frame() # draw Frame widget as Notebook
    Label1 = Label(mainframe, text="BIOS Scripts")
    b1 = Button(mainframe, text="BIOS Script 1", command=lambda: BIOSScript1(mainframe, master))
    b2 = Button(mainframe, text="BIOS Script 2", command=lambda: BIOSScript2(mainframe, master))
    b3 = Button(mainframe, text="BIOS Script 3", command=lambda: BIOSScript3(mainframe, master))
    b4 = Button(mainframe, text="BIOS Script 4", command=lambda: BIOSScript4(mainframe, master))
    b5 = Button(mainframe, text="BIOS Script 5", command=lambda: BIOSScript5(mainframe, master))
    b6 = Button(mainframe, text="BIOS Script 6", command=lambda: BIOSScript6(mainframe, master))
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    Label(mainframe, text="BIOS Scripts").grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky=W)
    b1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    b2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    b3.grid(row=1, column=2, padx=5, pady=5, sticky=W)
    b4.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    b5.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    b6.grid(row=2, column=2, padx=5, pady=5, sticky=W)
    ReturnButton.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky=W)
    mainframe.pack()
        
def center(win): #Centers the program window
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))



    
master.geometry('{}x{}'.format(400, 250)) #Set window size
#master.resizable(width=False, height=False) #Make it so user can't resize window
#Logo
path = ".\images\BigBallerBrand.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Tkinter.Label(master, image = img)
panel.pack(fill=BOTH, expand=1, side=TOP, pady=5)

DrawMainScreen(master)
center(master)
master.mainloop() #The mainloop handles all the events that occur in a tkinter window, from button pressing to the commands that a button runs, very important