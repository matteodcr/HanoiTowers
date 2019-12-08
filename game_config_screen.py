import tkinter as tk
from random import randint

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80

class GameConfigScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        
        tk.Label(self, text="Nom").pack()
        
        randname = 'Player' + str(randint(0, 999)).ljust(3, '0')

        namevar = tk.StringVar(value=randname)
        tk.Entry(self, textvariable=namevar).pack()

        nvar = tk.IntVar()
        tk.Scale(self, variable = nvar, orient='horizontal', from_=2, to=20).pack()
        
        button_play = tk.Button(self, text="OK", command=lambda: self.collect(nvar, namevar, controller))
        button_play.pack()


    def collect(self, nvar, namevar, controller):
        from game_screen import GameScreen

        controller.show_frame(
            GameScreen,
            name=namevar.get(),
            n=int(nvar.get()),
        )
