import tkinter as tk

from game_config_screen import GameConfigScreen
from game_screen import GameScreen
from main_screen import MainScreen
from storage import Storage


class Window(tk.Tk):
    '''
    Cette classe représente la fenêtre de jeu. Elle peut servir de conteneur 
    pour différents écrans - "Screen". Il en existe 3:
    
    - MainScreen (écran principal)
    - GameConfigScreen (écran de paramétrage du jeu juste avant une partie)
    - GameScreen (écran de jeu, contient un canvas turtle)
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Hanoï Simulator 2019')
        self.resizable(width=False, height=False)
        self.geometry('600x360')

        self.last_frame = None

        self.storage = Storage()

        container = tk.Frame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack(side="top", fill="both", expand=True)
        self.container = container

        self.show_frame(MainScreen)


    def show_frame(self, F, **kwargs):
        '''
        Met à jour l'écran affiché dans la fenêtre.
        F est une classe d'un écran (exemple "MainScreen")
        '''

        if self.last_frame != None: self.last_frame.grid_remove()

        # On instancie l'écran et on le positionne dans la fenêtre
        frame = F(parent=self.container, controller=self, **kwargs)
        frame.grid(row=0, column=0, sticky="nsew")

        self.last_frame = frame
