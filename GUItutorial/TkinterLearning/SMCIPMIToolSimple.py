'''
Created on Oct 2, 2017

@author: Iceman
'''
import os
import Tkinter as tk
from Tkinter import *
from ttk import Notebook
import tkMessageBox
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

class App:

    def __init__(self, master):
        
        # Main Tab
        tab1 = Frame(note)
        note.add(tab1, text="IPMI")
        Label(tab1, text="IPMI IP Address").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        Label(tab1, text="Username").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        Label(tab1, text="Password").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        Label(tab1, text="Command").grid(row=3, column=0, padx=5, pady=5, sticky=W)
        Label(tab1, text="IPMI Scripts").grid(row=5, column=1, padx=5, pady=5)
        '''ip = "172.16.99.101"#StringVar()
        user= "ADMIN"#StringVar()
        pw = "ADMIN"#StringVar()
        cmd = "ipmi ver"#StringVar()
        e1 = Entry(tab1, textvariable=ip).grid(row=0, column=1)
        e2 = Entry(tab1, textvariable=user).grid(row=1, column=1)
        e3 = Entry(tab1, textvariable=pw).grid(row=2, column=1)
        e4 = Entry(tab1, textvariable=cmd).grid(row=3, column=1)'''
# god dammit, finally figured out why I couldn't use e1.get before, because I combined .grid in same line!
        e1 = Entry(tab1) # IP Address
        e1.grid(row=0, column=1)
        e2 = Entry(tab1) # username
        e2.grid(row=1, column=1)
        e3 = Entry(tab1) # password
        e3.grid(row=2, column=1)
        e4 = Entry(tab1) # command
        e4.grid(row=3, column=1)
        b1 = Button(tab1, text="Test IP", command=lambda: self.testipmi(e1.get())).grid(row=6, column=0, padx=5, pady=5, sticky=W)
        b2 = Button(tab1, text="SMCIPMITool", command=lambda: self.SMC(e1.get(), e2.get(), e3.get(), e4.get())).grid(row=6, column=1, padx=5, pady=5, sticky=W)
        
        note.pack()
        
    def SMC(self, e1, e2, e3, e4):
        cmd = ".\SMCtool\SMCIPMITool.exe"
        os.system(' '.join([cmd, e1, e2 , e3, e4]))
        
    def ping(self, host):
        """
        Returns True if host (str) responds to a ping request.
        Remember that some hosts may not respond to a ping request even if the host name is valid.
        """
    
        # Ping parameters as function of OS
        parameters = "-n 1 -w 2000" if system_name().lower()=="windows" else "-c 1 -w 2000"
    
        # Pinging
        return system_call("ping " + parameters + " " + host)
    
    def testipmi(self, master):
        hostname = master
        response = self.ping(hostname)
        if response == 0:
            tkMessageBox.showinfo("Pingable", master + " is up")
        else:
            tkMessageBox.showinfo("Error", master + " can't be pinged")

def center(win): #Centers the program window
    win.update_idletasks()
    w = win.winfo_screenwidth()
    h = win.winfo_screenheight()
    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    win.geometry("%dx%d+%d+%d" % (size + (x,y)))

root = tk.Tk()
note = Notebook(root)
app = App(root)
center(root)
root.mainloop()