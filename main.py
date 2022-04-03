from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from time import sleep
from os import listdir

class Reader:

    def __init__(self) -> None:
        
        with open("config.txt", "r") as cfg:

            self.folder = cfg.readline().replace("folder: ", "").replace("\n", "")
    
            if self.folder == "None":
                self.not_defined_folder()
            
    def osu_reader(self):
        self.window = Tk()
        self.popup.title("osu! music reader")
        arr = listdir(self.osufolder.get())

                
    def not_defined_folder(self):
        self.popup = Tk()
        self.popup.title("Folder location")
        mainframe = ttk.Frame(self.popup, padding="1 4 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.osufolder = StringVar()
        self.osufolder.set("None")

        ttk.Label(mainframe, text="Choose your osu! folder location").grid(column=1, row=1)
        ttk.Button(mainframe, text="clicc", command=self.askdirectory).grid(column=1, row=2)
        ttk.Label(mainframe, textvariable=self.osufolder).grid(column=1, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="OK", command=self.popup.destroy).grid(column=1, row=4)
        self.popup.mainloop()
    
    def askdirectory(self):
        self.osufolder.set(filedialog.askdirectory())
        self.popup.update()

a = Reader()
