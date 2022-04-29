from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from time import sleep
from os import listdir
from itertools import *
from pygame import mixer

class Reader:

    def __init__(self) -> None:

        mixer.init()
        self.reader = Tk()
        self.previous_music = None
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

        else:
            self.update_list()
            
        self.reader.mainloop()


    def not_defined_folder(self, *args):

        self.popup = Toplevel()
        self.popup.title("Folder location")
        mainframe = ttk.Frame(self.popup, padding="1 4")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Choose your osu! folder location").grid(column=1, row=1)
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
        self.music_selection_menu = ttk.Frame(self.mainframe, padding=f"1 1 12 12").grid(column=2, row=2)

        musics_var = StringVar(value=self.arr)
        self.musics_list = Listbox(self.music_selection_menu, listvariable=musics_var, height=20, selectmode="browse")
        self.musics_list.grid(column=0, row=0, sticky=(N,W,E,S)) 
        self.musics_list.bind('<<ListboxSelect>>', self.play_music)


    def play_music(self, event):

        if self.previous_music != None:
            self.previous_music.stop()
            self.is_song_playing = False

        music_index = self.arr[self.musics_list.curselection()[0]]
        music_path = self.osufolder.get() + "/Songs/" + music_index

        folder = listdir(music_path)

        for file in folder:

            if ".mp3" in file:
                audio = music_path + "/" + file
                break

        self.player = mixer.Sound(file=audio)
        self.player.play()
        self.previous_music = self.player
        self.is_song_playing = True;

a = Reader()