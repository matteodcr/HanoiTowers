from turtle import *
from partieA import *
from partieB import *
from jeu import *


def main():
    n = int(numinput("Valeurs des disques", "Quelle est le nombre de disques ?"))
    game = Jeu(n)
    up()
    plateau = init(n)
    dessine_plateau(n)
    game.dessine_config(n)
    print(game.boucle_jeu(n))


speed(20)
main()
