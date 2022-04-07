from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from time import sleep
from os import listdir
from itertools import *
from vlc import *

class Reader:

    def __init__(self) -> None:

        self.reader = Tk()
        self.reader.title("osu! music reader")

        self.width = self.reader.winfo_screenwidth()
        self.height = self.reader.winfo_screenheight()
        self.reader.geometry(f"{self.width}x{self.height}")

        try:
            self.open_cfg()

        except FileNotFoundError:
            with open("config.txt", "x") as cfg:
                cfg.write("folder: None")

            self.open_cfg()


    def open_cfg(self):
        with open("config.txt", "r") as cfg:

            self.osufolder = StringVar()
            self.osufolder.set(cfg.readline().replace("folder: ", "").replace("\n", ""))
            self.osu_reader()


    def osu_reader(self):

        self.mainframe = ttk.Frame(self.reader, padding="2 2")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

        if self.osufolder.get() == "None":
            popup_gen = ttk.Label(self.mainframe, text="You haven't defined a folder yet! Click the button below to choose it!")
            popup_gen.grid(column=1, row=1)
            button = ttk.Button(self.mainframe, text="clicc", command= lambda: self.not_defined_folder(popup_gen, button))
            button.grid(column=1, row=2)
            
        self.reader.mainloop()


    def not_defined_folder(self, *args):

        self.popup = Toplevel()
        self.popup.title("Folder location")
        mainframe = ttk.Frame(self.popup, padding="1 4 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Choose your osu! folder location").grid(column=1, row=1)
        ttk.Button(mainframe, text="clicc", command=self.askdirectory).grid(column=1, row=2)
        ttk.Label(mainframe, textvariable=self.osufolder).grid(column=1, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="OK", command= lambda: [self.update_list(args), self.popup.destroy()]).grid(column=1, row=4)
        self.popup.mainloop()


    def askdirectory(self):

        self.osufolder.set(filedialog.askdirectory())
    

    def update_list(self, *args):
        
        for i in args[0]:
            i.destroy()

        self.arr = listdir(self.osufolder.get() + "/Songs/")
        self.music_selection_menu = ttk.Frame(self.mainframe, padding=f"1 {len(self.arr)}").grid(column=2, row=2)
        scrollbar = ttk.Scrollbar(self.music_selection_menu, orient="vertical")
        scrollbar.grid(column=1)

        for i,j in enumerate(self.arr):

            self.arr[i] = self.osufolder.get() + "/Songs/" + j

            ttk.Button(self.music_selection_menu, text=self.arr[i], command= lambda: self.play_music(self.arr[i])).grid(column=0, row=i+1, sticky=(W))
        
        print(self.arr)
    

    def play_music(self, path):

        print(path)
        for file in path:

            if ".mp3" in file:
                audio = file

        p = MediaPlayer(file)
        p.play()

        p.stop()

a = Reader()
