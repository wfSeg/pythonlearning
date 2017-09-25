'''
Created on Sep 21, 2017

@author: Ye
'''

from Tkinter import *

master = Tk() #Declaring of main window

def ProceedButtonCommand(mainframe, master): #Command to attach to proceed button
    mainframe.destroy()
    DrawSecondScreen(master) #This line is what lets the command tied to the button call up the second screen

def QuitButtonCommand(master):
    master.destroy()
    
def ReturnButtonCommand(mainframe, master): #Command to attach to return button
    mainframe.destroy()
    DrawFirstScreen(master)
    
def DrawFirstScreen(master):
    mainframe = Frame(master) #This is a way to semi-cheat when drawing new screens, destroying a frame below master frame clears everything from the screen without having to redraw the window, giving the illusion of one seamless transition
    ProceedButton = Button(mainframe, text="Proceed", command=lambda: ProceedButtonCommand(mainframe, master)) #Lambda just allows you to pass variables with the command
    QuitButton = Button(mainframe, text = "Quit", command=lambda: QuitButtonCommand(master))
    mainframe.pack()
    ProceedButton.pack()
    QuitButton.pack()
        
def DrawSecondScreen(master):
    mainframe = Frame(master)
    Label1 = Label(mainframe, text="Temp")
    #add in Return Button
    ReturnButton = Button(mainframe, text="Return", command=lambda: ReturnButtonCommand(mainframe, master))
    mainframe.pack()
    ReturnButton.pack()
    Label1.pack()
    
DrawFirstScreen(master)
master.mainloop() #The mainloop handles all the events that occur in a tkinter window, from button pressing to the commands that a button runs, very important