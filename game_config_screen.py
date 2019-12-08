import tkinter as tk

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80

class GameConfigScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        
        tk.Label(self, text="Nom").pack()
        
        namevar = tk.StringVar()
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
