#Librairies
from turtle import *
from numpy import *

from partieA import *
from partieB import *
from partieC import *

speed(20)

def main():
    n = int(numinput("Valeurs des disques", "Quelle est le nombre de disques ?"))
    plateau = init(n)
    dessine_plateau(n)
    dessine_config(plateau, n)
    boucle_jeu(plateau, n)



main()





    
    

    
        







  


