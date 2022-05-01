from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from time import sleep
from os import listdir
from itertools import *
from pygame import mixer
from random import *

class Reader:

    def __init__(self) -> None:

        mixer.init()
        self.player = None
        self.reader = Tk()
        self.reader.title("osu! music reader")
        self.width = self.reader.winfo_screenwidth()
        self.height = self.reader.winfo_screenheight()
        self.reader.geometry(f"{self.width}x{self.height}")
        self.music = StringVar()
        self.is_playing = StringVar()

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

        else:
            self.update_list()
            self.random_music = ttk.Button(self.mainframe, text="random music", command= lambda: self.play_random_music())
            self.random_music.grid(column=0, row=1)
            self.sb = Scrollbar(self.mainframe, orient=VERTICAL, command=self.musics_list.yview)
            self.sb.grid(column=1, row=0, sticky=(N,S))
            self.indicator = ttk.Label(self.mainframe, textvariable=self.music)
            self.indicator.grid(row=2, column=0)
            
        self.reader.mainloop()


    def not_defined_folder(self, *args):

        self.popup = Toplevel()
        self.popup.title("Folder location")
        mainframe = ttk.Frame(self.popup, padding="4 4")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Choose your osu! folder location").grid(column=0, row=0)
        ttk.Button(mainframe, text="clicc", command=self.askdirectory).grid(column=1, row=2)
        ttk.Label(mainframe, textvariable=self.osufolder).grid(column=1, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="OK", command= lambda: [self.update_list(args), self.popup.destroy()]).grid(column=1, row=4)
        self.popup.mainloop()


    def askdirectory(self):

        self.osufolder.set(filedialog.askdirectory())
    

    def update_list(self, *args):
        
        if len(args) != 0:
            for i in args[0]:
                i.destroy()

        self.arr = listdir(self.osufolder.get() + "/Songs/")

        musics_var = StringVar(value=self.arr)
        self.musics_list = Listbox(self.mainframe, listvariable=musics_var, height=20, selectmode="browse")
        self.musics_list.grid(column=0, row=0, sticky=(W,E)) 
        self.musics_list.bind('<Double-Button-1>', self.play_music)


    def play_music(self, event):

        if self.player != None:
            self.player.stop()

        music_index = self.arr[self.musics_list.curselection()[0]]
        music_path = self.osufolder.get() + "/Songs/" + music_index

        folder = listdir(music_path)

        for file in folder:

            if ".mp3" in file:
                audio = music_path + "/" + file
                break

        self.player = mixer.Sound(file=audio)
        self.player.play()
        self.music.set(audio)


    def play_random_music(self):

        if self.player != None:
            self.player.stop()

        music_index = randint(0, len(self.arr))
        music_name = self.arr[music_index]
        music_path = self.osufolder.get() + "/Songs/" + music_name

        folder = listdir(music_path)

        for file in folder:

            if ".mp3" in file:
                audio = music_path + "/" + file
                break

        self.player = mixer.Sound(file=audio)
        self.player.play()
        self.music.set(audio)
    
    """def pause_play_music(self):"""
        

a = Reader()