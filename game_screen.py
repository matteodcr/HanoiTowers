import tkinter as tk
from turtle import RawTurtle

from jeu import Jeu
from partieB import dessine_plateau
from turtle_utils import set_turtle


class GameScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.first_tower = None
        self.last_tower = None

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
        game = Jeu(3)
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
        cancel_button = tk.Button(buttons_frame, command=lambda: self.game.annuler_dernier_coup(game.coups, game.coups_index), bitmap='error'  ,bg='red')
        cancel_button.grid(row=1, column=0, columnspan = 3, sticky='nesw')

        


    def button_play(self):
        ''' Verifie si le deplacement est possible et le réalise si c'est le cas '''
        if self.game.verifier_deplacement(self.first_tower, self.last_tower) == False :
            print('Deplacement impossible, veuillez réessayer.')
            return None, None
        else :
            finished, message = self.game.jouer_un_coup(self.first_tower, self.last_tower)
            return finished, message
   
    def button_press(self, index: int):
        ''' Enregistre quel bouton est pressé'''
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
        print('Fin', message)
