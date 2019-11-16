#Librairies
from turtle import *
from numpy import *

from partieA import *
from partieB import *
from partieC import *



def main(n):
    plateau = init(n)
    dessine_plateau(n)
    dessine_config(plateau, n)
    boucle_jeu(plateau, n)

main(3)

    
    

    
        







  


