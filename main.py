#Librairies
from turtle import *

from partieA import *
from partieB import *
from partieC import *

speed(20)

def main():
    n = int(numinput("Valeurs des disques", "Quelle est le nombre de disques ?"))
    #plateau = [[3], [], [2, 1]]
    up()
    plateau = init(n)
    dessine_plateau(n)
    dessine_config(plateau, n)
    boucle_jeu(plateau, n)
    input('ceci sert à empecher que la fenetre se ferme apres exec')
    
main()
