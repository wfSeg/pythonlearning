'''
Created on Sep 25, 2017

@author: Rachel McAdams
'''
from Tkinter import *

class notebook:
    #initialization. receives master widget
    #ref and the notebook orientation
    def __init__(self, master, side=LEFT):
        
        self.active_fr = None
        self.count = 0
        self.choice = IntVar(0)
        