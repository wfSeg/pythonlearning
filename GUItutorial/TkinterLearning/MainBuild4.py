'''
Created on Sep 28, 2017

@author: Dumbledore
'''

# Change everything from Build3 to a Class App?

import Tkinter as tk
from Tkinter import *
from ttk import Notebook
import os
import tkMessageBox
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

class App:

    def __init__(self, master):
        
        # Main Tab
        tab1 = Frame(note)
        note.add(tab1, text="Main")
        self.quit = Button(tab1, text = "Quit", command=quit).grid(row=0, column=0)
        self.hi_there = Button(tab1, text="Hello", command=self.say_hi).grid(row=0, column=1)
        
        # IPMI Tab
        tab2 = Frame(note)
        note.add(tab2, text="IPMI")
        Label(tab2, text="IPMI IP Address").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        Label(tab2, text="Username").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        Label(tab2, text="Password").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        Label(tab2, text="IPMI Scripts").grid(row=4, column=1, padx=5, pady=5)
        ip = StringVar()
        e1 = Entry(tab2, textvariable=ip).grid(row=0, column=1)
        e2 = Entry(tab2).grid(row=1, column=1)
        e3 = Entry(tab2).grid(row=2, column=1)
        testbutton = Button(tab2, text="test", command=lambda: self.testipmi(ip)).grid(row=0, column=2, padx=5, pady=5, sticky=W)
        b1 = Button(tab2, text="IPMI Script 1", command=lambda: self.IPMIScript1(master)).grid(row=5, column=0, padx=5, pady=5, sticky=W)
        b2 = Button(tab2, text="IPMI Script 2", command=lambda: self.IPMIScript2(master)).grid(row=5, column=1, padx=5, pady=5)
        b3 = Button(tab2, text="IPMI Script 3", command=lambda: self.IPMIScript3(master)).grid(row=5, column=2, padx=5, pady=5, sticky=E)
        b4 = Button(tab2, text="IPMI Script 4", command=lambda: self.IPMIScript4(master)).grid(row=6, column=0, padx=5, pady=5, sticky=W)
        b5 = Button(tab2, text="IPMI Script 5", command=lambda: self.IPMIScript5(master)).grid(row=6, column=1, padx=5, pady=5)
        b6 = Button(tab2, text="IPMI Script 6", command=lambda: self.IPMIScript6(master)).grid(row=6, column=2, padx=5, pady=5, sticky=E)
        
        # BIOS Tab
        tab3 = Frame(note)
        note.add(tab3, text="BIOS")
        Label1 = Label(tab3, text="BIOS Scripts")
        Label(tab3, text="BIOS Scripts").grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky=W)
        b1 = Button(tab3, text="BIOS Script 1", command=lambda: self.BIOSScript1(master)).grid(row=1, column=0, padx=5, pady=5, sticky=W)
        b2 = Button(tab3, text="BIOS Script 2", command=lambda: self.BIOSScript2(master)).grid(row=1, column=1, padx=5, pady=5, sticky=W)
        b3 = Button(tab3, text="BIOS Script 3", command=lambda: self.BIOSScript3(master)).grid(row=1, column=2, padx=5, pady=5, sticky=W)
        b4 = Button(tab3, text="BIOS Script 4", command=lambda: self.BIOSScript4(master)).grid(row=2, column=0, padx=5, pady=5, sticky=W)
        b5 = Button(tab3, text="BIOS Script 5", command=lambda: self.BIOSScript5(master)).grid(row=2, column=1, padx=5, pady=5, sticky=W)
        b6 = Button(tab3, text="BIOS Script 6", command=lambda: self.BIOSScript6(master)).grid(row=2, column=2, padx=5, pady=5, sticky=W)
             

        note.pack()

    def say_hi(self):
        tkMessageBox.showinfo("About", "GUI for python scripts")
    def IPMIScript1(self, master):
        os.system('python DraftPick.py')
    def IPMIScript2(self, master):
        os.system('python pyinsidepy.py')
    def IPMIScript3(self, master):
        os.system('python hellowhat.py')
    def IPMIScript4(self, master):
        os.system('python ButtonToOpenNewMenu.py')
    def IPMIScript5(self, master):
        os.system('python helloworld.py')
    def IPMIScript6(self, master):
        os.system('python FrameExample.py')
    def BIOSScript1(self, master):
        os.system('python pyinsidepy.py')
    def BIOSScript2(self, master):
        os.system('python hellowhat.py')
    def BIOSScript3(self, master):
        os.system('python DraftPick.py')
    def BIOSScript4(self, master):
        os.system('python ButtonToOpenNewMenu.py')
    def BIOSScript5(self, master):
        os.system('python NotebookTestmockup.py')
    def BIOSScript6(self, master):
        os.system('python TheNotebook.py')
        
    def ping(self, host):
        """
        Returns True if host (str) responds to a ping request.
        Remember that some hosts may not respond to a ping request even if the host name is valid.
        """
    
        # Ping parameters as function of OS
        parameters = "-n 1 -w 2000" if system_name().lower()=="windows" else "-c 1 -w 2000"
    
        # Pinging
        return system_call("ping " + parameters + " " + host)
    
    def testipmi(self, ip):
        hostname = ip.get()
        response = self.ping(hostname)
        if response == 0:
            tkMessageBox.showinfo("Score!", ip.get() + " is up")
        else:
            tkMessageBox.showinfo("Airball", ip.get() + " can't be pinged")    
# Added Logo
from PIL import Image, ImageTk
class Logo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open('BigBallerBrand.jpg')
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
        
class center(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        self.geometry("%dx%d+%d+%d" % (size + (x,y)))

root = tk.Tk()
root.title("testbuild")
Logo(root)
note = Notebook(root)
center(root)
app = App(root)

root.mainloop()
