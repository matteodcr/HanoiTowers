from game_config_screen import GameConfigScreen
import tkinter as tk


BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80

class MainScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        button_play = tk.Button(self, text="Jouer", command=lambda: controller.show_frame(GameConfigScreen))
        button_play.pack()



