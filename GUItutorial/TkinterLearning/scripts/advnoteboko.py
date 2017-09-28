'''
Created on Sep 27, 2017

@author: Gimli
'''
from Tkinter import ttk
from Tkinter import *
from Tkinter.ttk import *

mainframe = Tk()

tabs = ttk.Notebook(mainframe, width=319, height=210, style=style.Notebook)
tabs.grid(column=0, row=1, sticky=('n', 'w', 'e', 's'))
tabs.columnconfigure(0, weight=1)
tabs.rowconfigure(0, weight=1)

tab1 = ttk.Frame(tabs)
tab1_frame = ttk.Frame(tab1, style=style.Frame)
tab1_frame.pack(anchor='center', expand=1, fill='both')
# stick some widgets in
progress = ttk.Progressbar(tab1_frame, orient="horizontal", length=300, mode="determinate")
progress.grid(column=1, row=1, columnspan=2, padx=style.padding, pady=style.padding)
progress['maximum'] = 1000
progress['value'] = 500
# More widgets
# Another tab
tab2 = ttk.Frame(tabs)
tab2_frame = ttk.Frame(tab2, style=style.Frame)
tab2_frame.pack(anchor='center', expand=1, fill='both')
# blah blah

style_config = Style()
style_config.theme_use('default')

style_config.configure(self.Notebook,
    background=self.dark,
    borderwidth=0)

style_config.configure(self.Tab,
   background=self.dark,
   foreground='white',
   padding=self.padding,
   borderwidth=0)
style_config.map(self.Tab,
    background=[('selected', self.color1)])

mainframe.mainloop()