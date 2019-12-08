import time
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import RawTurtle

from jeu import Jeu
from main_screen import MainScreen
from partieB import dessine_plateau
from turtle_utils import set_turtle


class GameScreen(tk.Frame):

    def __init__(self, parent, controller, n, name):
        super().__init__(parent)

        # On expose le controlleur au reste de la classe pour pouvoir naviguer
        self.controller = controller

        self.first_tower = None
        self.last_tower = None

        # Utilisé à la fin du jeu pour les scores
        self.name = name
        self.start_time = None

        self.columnconfigure(0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1, minsize=40)

        # Placement de la Frame de turtle et de celle qui contient les boutons
        frame1 = tk.Frame(self)
        frame2 = tk.Frame(self)
        frame1.grid(row=0, column=0)
        frame2.grid(row=1, column=0)

        canvas = tk.Canvas(frame1, width=600, height=300)
        turtle = RawTurtle(canvas)
        turtle.up()
        turtle.speed(1000)
        set_turtle(turtle)
        canvas.grid()

        # On initialise le jeu
        game = Jeu(n)
        dessine_plateau(game.n)
        game.dessine_config()
        self.game = game

        # Placement de la Frame qui contient les boutons
        buttons_frame = tk.Frame(frame2,  bg='red')
        buttons_frame.grid(sticky='nesw')

        # Placement des boutons pour les tours
        tk.Button(buttons_frame, text="     1     ", command=lambda: self.button_press(0)).grid(row=0, column=0, sticky='nesw')
        tk.Button(buttons_frame, text="     2     ", command=lambda: self.button_press(1)).grid(row=0, column=1, sticky='nesw')
        tk.Button(buttons_frame, text="     3     ", command=lambda: self.button_press(2)).grid(row=0, column=2, sticky='nesw')
        cancel_button = tk.Button(buttons_frame, text='Annuler', command=lambda: self.game.annuler_dernier_coup(game.coups, game.coups_index), bg='red')
        cancel_button.grid(row=1, column=0, columnspan = 3, sticky='nesw')


    def button_play(self):
        ''' Verifie si le deplacement est possible et le réalise si c'est le cas '''

        if self.game.verifier_deplacement(self.first_tower, self.last_tower) == False:
            print('Deplacement impossible, veuillez réessayer.')
            return None, None
        else:
            finished, message = self.game.jouer_un_coup(self.first_tower, self.last_tower)
            return finished, message


    def button_press(self, index: int):
        ''' Enregistre quel bouton est pressé '''

        # Si c'est le premier coup, on lance le timer
        if self.start_time is None:
            self.start_time = time.time()

        # Si le joueur designe la tour de depart
        if self.first_tower == None:
            self.first_tower = index

        # Si le joueur designe la tour de d'arrivée
        else:
            self.last_tower = index
            finished, message = self.button_play()
            self.first_tower = None
            self.last_tower = None

            if finished:
                self.on_game_finished(message)


    def on_game_finished(self, message: str):
        from main_screen import MainScreen

        if message == "Gagné":
            game_length = time.time() - self.start_time
            self.controller.storage.append_score(
                self.name,
                self.game.n,
                self.game.coups_index,
                game_length,
            )

        tkm.showinfo('Jeu terminé', message)
        self.controller.show_frame(MainScreen)
