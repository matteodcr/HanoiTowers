import tkinter as tk
from turtle import RawTurtle

from jeu import Jeu
from partieB import dessine_plateau
from turtle_utils import set_turtle


class GameScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.last_button = None

        self.columnconfigure(0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1, minsize=40)

        frame1 = tk.Frame(self)
        frame2 = tk.Frame(self)

        canvas = tk.Canvas(frame1, width=600, height=360)
        turtle = RawTurtle(canvas)
        turtle.up()
        turtle.speed(1000)
        set_turtle(turtle)
        canvas.pack()

        game = Jeu(3)
        dessine_plateau(game.n)
        game.dessine_config()
        self.game = game

        buttons_frame = tk.Frame(frame2)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.columnconfigure(2, weight=1)
        buttons_frame.rowconfigure(0)

        tk.Button(buttons_frame, text="1", command=lambda: self.button_press(0)).grid(row=0, column=0, sticky='we')
        tk.Button(buttons_frame, text="2", command=lambda: self.button_press(1)).grid(row=0, column=1, sticky='we')
        tk.Button(buttons_frame, text="3", command=lambda: self.button_press(2)).grid(row=0, column=2, sticky='we')

        buttons_frame.pack(fill=tk.X, expand=tk.YES, anchor='s')

        frame1.grid(row=0, column=0)
        frame2.grid(row=1, column=0)
    
    def button_press(self, index: int):
        if self.last_button is None:
            self.last_button = index
        else:
            finished, message = self.game.jouer_un_coup(self.last_button, index)
            self.last_button = None
            if finished:
                self.on_game_finished(message)
    
    def on_game_finished(self, message: str):
        print('Fin', message)
