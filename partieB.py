from turtle import *
from numpy import *
from partieA import *

#rajouter def square pour simplifier


def LargeurPGDisque(n): #ok
    '''Renvoie la largeur du plus grand disque en fonction de n'''
    return (40+30*(n))

def base(n):
    '''dessine la base en fonction de n'''
    down()
    for i in range(0,2):
        forward(120+3*LargeurPGDisque(n))
        right(90)
        forward(20)
        right(90)
    up()

def tour(n): #ok
    '''dessine une tour'''

    down()

    dep = ((120+3*LargeurPGDisque(n))/6)-3
    forward(dep)
    left(90)
    forward((n+1)*20)
    right(90)
    forward(6)
    right(90)
    forward((n+1)*20)
    left(90)
    forward(dep)

    up()
        
def dessine_plateau(n): #ok
    '''fusion de base et tour x3'''
    up()
    goto(-300,200)
    down()

    base(n)
    for i in range(0,3):
        tour(n)



def dessine_disque(plateau, NumDisque, n, couleur): #ok
    '''dessine un disque specifique'''
    dep = (120+3*LargeurPGDisque(n))/6
    IndexTour, IndexDisque, len = position_disque(plateau,NumDisque)

    up()
    if IndexTour == 0 :
        goto((-300+dep),200)
    if IndexTour == 1 :
        goto((-300+3*dep),200)
    if IndexTour == 2 :
        goto((-300+5*dep),200)
    down()

    if couleur == 'noir':fillcolor('black')
    if couleur == 'blanc':fillcolor('white')
        
    begin_fill()
    left(90)
    up()
    forward(20*(IndexDisque+1))
    right(90)
    forward((40+30*NumDisque)/2)
    right(90)
    forward(20)
    right(90)
    forward(40+30*NumDisque)
    right(90)
    forward(20)
    right(90)
    forward((40+30*NumDisque)/2)
    end_fill()

def efface_disque(plateau, NumDisque, n,state): #ok
    '''efface un disque en utilisant dessine_disque mais en blanc'''
    down()
    dessine_disque(plateau, NumDisque, n, 'blanc')

    if state == 'single':
        goto(-300,200)
        for i in range(0,3):
            tour(n)
    up()

#plateau = [[2],[3],[1]]
#dessine_plateau(3)


def dessine_config(plateau, n): #ok
    '''dessine la config de depat'''
    down()
    for IndexTour in range(0,len(plateau)):
        l = list(plateau[IndexTour])
        for i in range(0,len(l)) :
            dessine_disque(plateau, l[i],n,'noir')
    up()


     
def efface_tout(plateau, n): #ok
    down()

    for IndexTour in range(0,len(plateau)):
        l = list(plateau[IndexTour])
        for i in range(0,len(l)):
            efface_disque(plateau, l[i],n, 'yesai')

        goto(-300,200)
    for i in range(0,3):
        tour(n)
    up()


