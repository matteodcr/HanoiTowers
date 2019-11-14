#Librairies
from turtle import *
from numpy import *

from partieA import *
from partieB import *

#n = int(input('Entrez votre valeur n : '))

def main(n):
    plateau=init(n)
    dessine_plateau(n)
    dessine_config(plateau,n)
    efface_tout(plateau, n)
    
main(4)
    
        







  


