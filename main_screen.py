import tkinter as tk

from game_config_screen import GameConfigScreen

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 80

class MainScreen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        button_play = tk.Button(self, text="Jouer", command=lambda: controller.show_frame(GameConfigScreen))
        button_play.pack()

        scores = controller.storage.get_scores_sorted()
        scores_formatted = ['{}: {} disques - {}s ({} s/coup)'.format(
            s[0],
            s[1],
            round(s[3], 2),
            round(s[3] / s[2], 2),
        ) for s in scores]

        credit = tk.Label(self, text='\n'.join(scores_formatted), justify=tk.LEFT)
        credit.pack()
