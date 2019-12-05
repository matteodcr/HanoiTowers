import tkinter as tk

from game_config_screen import GameConfigScreen
from game_screen import GameScreen
from main_screen import MainScreen


class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Hanoï Simulator 2019')
        self.resizable(width=False, height=False)
        self.geometry('600x360')

        self.last_frame = None

        container = tk.Frame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack(side="top", fill="both", expand=True)
        self.container = container

        self.show_frame(MainScreen)

    def show_frame(self, F, **kwargs):
        '''Show a frame for the given page name'''
        if self.last_frame != None: self.last_frame.grid_remove()
        frame = F(parent=self.container, controller=self, **kwargs)
        frame.grid(row=0, column=0, sticky="nsew")
        self.last_frame = frame
