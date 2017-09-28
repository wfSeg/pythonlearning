'''
Created on Sep 25, 2017

@author: Sun Wukong
'''

#!/usr/bin/python

import Tkinter as tk

class Application:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()    
        self.okButton = tk.Button(self.frame, text="OK",
                                  command=self.window_maker).pack()
        self.BIOS1Button = tk.Button(self.frame, text="BIOS1Script",
                                     command=self.script1).pack()
        self.quitButton = tk.Button(self.frame, text="Close",
                                    command=self.frame.quit).pack()
    def window_maker(self):
        MakeWindow("A message to Toplevel")
    def script1(self):
        script1("hello")


class MakeWindow(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self) 
        self.message = message
        self.display = tk.Label(self, text=message)
        self.display.pack()
class script1(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self)
        self.message = message
        self.display = tk.Label(self, text=message)
        self.display.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()