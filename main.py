from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from time import sleep
from os import listdir
from itertools import *

class Reader:

    def __init__(self) -> None:
        
        self.reader = Tk()
        self.reader.title("osu! music reader")
        self.reader.geometry(f"{self.reader.winfo_screenwidth()}x{self.reader.winfo_screenheight()}")

        try:
            self.open_cfg()

        except FileNotFoundError:
            with open("config.txt", "x") as cfg:
                cfg.write("folder: None")
            
            self.open_cfg()

    def osu_reader(self):
        arr = listdir(self.osufolder.get())
        mainframe = ttk.Frame(self.reader, padding="2 2")
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

        music_selection_menu = ttk.Frame(mainframe, padding=f"1 {len(arr)}").grid(column=2, row=2)
        
        for i,j in enumerate(arr):
            ttk.Label(music_selection_menu, text=j).grid(column=1, row=i, sticky=(W))
        
        self.reader.mainloop()
                
    def not_defined_folder(self):
        self.popup = Toplevel()
        self.popup.title("Folder location")
        mainframe = ttk.Frame(self.popup, padding="1 4 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Choose your osu! folder location").grid(column=1, row=1)
        ttk.Button(mainframe, text="clicc", command=self.askdirectory).grid(column=1, row=2)
        ttk.Label(mainframe, textvariable=self.osufolder).grid(column=1, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="OK", command=self.popup.quit).grid(column=1, row=4)
        self.popup.mainloop()
    
    def askdirectory(self):
        self.osufolder.set(filedialog.askdirectory())
        self.popup.update()
    
    def open_cfg(self):
        with open("config.txt", "r") as cfg:
            self.osufolder = StringVar()
            self.osufolder.set(cfg.readline().replace("folder: ", "").replace("\n", ""))

            if self.osufolder.get() == "None":
                self.not_defined_folder()
        
            self.osu_reader()


a = Reader()
