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
def BIOSScript3(mainframe, master):
    os.system('python scripts/DraftPick.py')
def BIOSScript4(mainframe, master):
    os.system('python scripts/ButtonToOpenNewMenu.py')
def BIOSScript5(mainframe, master):
    os.system('python scripts/helloworld.py')
def BIOSScript6(mainframe, master):
    os.system('python scripts/sigh.py')
    
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
    BIOSScript3Button = Button(mainframe, text="BIOS Script 3", command=lambda: BIOSScript3(mainframe, master))
    BIOSScript4Button = Button(mainframe, text="BIOS Script 4", command=lambda: BIOSScript4(mainframe, master))
    BIOSScript5Button = Button(mainframe, text="BIOS Script 5", command=lambda: BIOSScript5(mainframe, master))
    BIOSScript6Button = Button(mainframe, text="BIOS Script 6", command=lambda: BIOSScript6(mainframe, master))
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    mainframe.pack()
    BIOSScript1Button.pack(side=LEFT)
    BIOSScript2Button.pack(side=LEFT)
    BIOSScript3Button.pack(side=LEFT)
    BIOSScript4Button.pack(side=BOTTOM)
    BIOSScript5Button.pack(side=BOTTOM)
    BIOSScript6Button.pack(side=BOTTOM)
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

from PIL import Image, ImageTk #For the Logo, automatically resizes it
class App(Frame):
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
   
 
master.geometry('{}x{}'.format(300, 300)) #Set window size
master.resizable(width=False, height=False) #Make it so user can't resize window

App(master)
DrawMainScreen(master)
center(master)
master.mainloop() #The mainloop handles all the events that occur in a tkinter window, from button pressing to the commands that a button runs, very important