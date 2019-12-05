from game_screen import GameScreen
import tkinter as tk


BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80

class GameConfigScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="Nom").pack()
        input_name = tk.Entry(self)
        input_name.pack()

        scale_n = tk.Scale(self, orient='horizontal', from_=2, to=20)
        scale_n.pack()

        button_play = tk.Button(self, text="OK", command=lambda: controller.show_frame(GameScreen))
        button_play.pack()

