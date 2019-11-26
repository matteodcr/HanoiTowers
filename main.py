from turtle import *

from partieA import *
from partieB import *
from partieC import *


def main():
    n = int(numinput("Valeurs des disques", "Quelle est le nombre de disques ?"))
    up()
    plateau = init(n)
    dessine_plateau(n)
    dessine_config(plateau, n)
    boucle_jeu(plateau, n)


speed(20)
main()
