from turtle import *
from numpy import *
from partieA import *
from turtle_utils import *


##CONSTANTES
LARGEUR_PETIT_DISQUE = 40
LARGEUR_TOUR = 6

##DEFINITION DES LONGUEURS EN FONCTION DE N
def largeur_disque(num_disque):
    return 40+30*num_disque
    
def largeur_pgdisque(n): #ok
    '''Renvoie la largeur du plus grand disque en fonction de n'''
    return (LARGEUR_PETIT_DISQUE+30*(n))

def largeur_base(n):
    return 3*(LARGEUR_PETIT_DISQUE+largeur_pgdisque(n))

def hauteur_tour(n):
    return (n+1)*20

def hauteur_disque(num_disque):

    return 20*(num_disque)

##DESSIN AVEC TURTLE
def base(n):
    '''dessine la base en fonction de n'''
    down()
    rect(largeur_base(n),20)
    up()
    
    return ((120+3*largeur_pgdisque(n))/6)-3

def dessine_tour(n): 
    '''dessine une tour'''
    tier_base = (largeur_base(n)/6)

    down()
    forward(tier_base)
    rect(6,hauteur_tour(n))
    forward(tier_base)
    up()
        
def dessine_plateau(n): #ok
    '''fusion de base et tour x3'''
    up()
    goto(-300,180)
    down()
    base(n)

    goto(-300,200)
    for i in range(0,3):
        dessine_tour(n)

def coord_disque(plateau, n, num_disque):

    tier_base = largeur_base(n)/6
    index_tour, index_disque, nb_disque_tour = position_disque(plateau,num_disque)

    up()
    if index_tour == 0 :
        goto((-300+tier_base),200)
    if index_tour == 1 :
        goto((-300+3*tier_base),200)
    if index_tour == 2 :
        goto((-300+5*tier_base),200)
    down()

    return index_disque


def dessine_disque(plateau, num_disque, n, couleur): 
    '''dessine un disque specifique'''

    if couleur == 'noir':fillcolor('black') #pour dessiner
    if couleur == 'blanc':fillcolor('white') #pour effacer

    index_disque = coord_disque(plateau, n, num_disque)

    up()
    forward((largeur_disque(num_disque)+LARGEUR_TOUR)/2)
    tourner_gauche()
    forward(hauteur_disque(index_disque))

    begin_fill()
    rect(20, largeur_disque(num_disque))
    end_fill()
    tourner_droite()


def efface_disque(plateau, n, num_disque, state): 
    '''efface un disque en utilisant dessine_disque mais en blanc'''
    down()
    dessine_disque(plateau, num_disque, n, 'blanc')

    if state == 'single':
        goto(-300,200)
        for i in range(0,3):
            dessne_tour(n)
    up()

def dessine_config(plateau, n): 
    '''dessine la config de depart'''
    down()
    for IndexTour in range(0,len(plateau)):
        l = list(plateau[IndexTour])
        for i in range(0,len(l)) :
            dessine_disque(plateau, l[i],n,'noir')
    up()


     
def efface_tout(plateau, n): 
    down()

    for IndexTour in range(0,len(plateau)):
        l = list(plateau[IndexTour])
        for i in range(0,len(l)):
            efface_disque(plateau, l[i],n, 'yesai')

        goto(-300,200)
    for i in range(0,3):
        tour(n)
    up()


