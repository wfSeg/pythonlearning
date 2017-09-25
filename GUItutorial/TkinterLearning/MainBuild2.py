'''
Created on Sep 25, 2017

@author: Kanye Southeast
'''
from Tkinter import *
import Tkinter
import os

master = Tk() #Declaring of main window
master.title("Superballer GUI") #Title for main window

def BIOSButtonCommand(mainframe, master): #Command to attach to proceed button
    mainframe.destroy()
    DrawSecondScreen(master) #call up the second screen

def QuitButtonCommand(master):
    master.destroy()
    
def ReturnButtonCommand(mainframe, master): #Command to attach to return button
    mainframe.destroy()
    DrawMainScreen(master)
    
#Put path/directory of scripts here, put .py in the /scripts folder
def BIOSScript1(mainframe, master):
    os.system('python scripts/canvashuh.py')
def BIOSScript2(mainframe, master):
    os.system('python scripts/hellowhat.py')
    
def DrawMainScreen(master):
    mainframe = Frame(master) #draw Frame widget
    BIOSButton = Button(mainframe, text="BIOS Scripts", command=lambda: BIOSButtonCommand(mainframe, master))
    QuitButton = Button(mainframe, text = "Quit", command=lambda: QuitButtonCommand(master))
    mainframe.pack()
    BIOSButton.pack(side=LEFT)
    QuitButton.pack(side=BOTTOM)
        
def DrawSecondScreen(master):
    mainframe = Frame(master)
    Label1 = Label(mainframe, text="BIOS Scripts")
    BIOSScript1Button = Button(mainframe, text="BIOS Script 1", command=lambda: BIOSScript1(mainframe, master))
    BIOSScript2Button = Button(mainframe, text="BIOS Script 2", command=lambda: BIOSScript2(mainframe, master))
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    mainframe.pack()
    BIOSScript1Button.pack(side=LEFT)
    BIOSScript2Button.pack(side=LEFT)
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

'''This sections is for organizing, and making the program look good
logos, positioning, and widgets organized here'''
    
from PIL import ImageTk, Image
#Logo
path = ".\images\BigBallerBrand.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Tkinter.Label(master, image = img)
panel.pack(side=BOTTOM, fill=BOTH, expand=YES)

master.geometry('{}x{}'.format(300, 300)) #Set window size
master.resizable(width=False, height=False) #Make it so user can't resize window

DrawMainScreen(master)
center(master)
master.mainloop() #The mainloop handles all the events that occur in a tkinter window, from button pressing to the commands that a button runs, very important