from partieA import *
from turtle_utils import *


LARGEUR_PETIT_DISQUE = 40
LARGEUR_TOUR = 6


def largeur_disque(num_disque) -> int:
    return 40 + 30 * num_disque


def largeur_pgdisque(n) -> int: #ok
    '''Renvoie la largeur du plus grand disque en fonction de n'''
    return (LARGEUR_PETIT_DISQUE + 30 * (n))


def largeur_base(n) -> int:
    return 3 * (LARGEUR_PETIT_DISQUE+largeur_pgdisque(n))


def hauteur_tour(n) -> int:
    return (n+1) * 20


def hauteur_disque(num_disque) -> int:
    return 20*(num_disque)


def base(n):
    '''dessine la base en fonction de n'''
    rect(0, 0, largeur_base(n), 20)


def dessine_tour(n, index: int): 
    '''dessine une tour'''
    third_width = largeur_base(n) / 3
    third_x = third_width * index
    offset = third_width / 2 - 3
    rect(third_x + offset, 20, 6, hauteur_tour(n))


def dessine_plateau(n):
    '''fusion de base et tour x3'''
    base(n)
    
    for i in range(0, 3):
        dessine_tour(n, i)


def dessine_disque(plateau, num_disque, n, color = 'black'): 
    '''dessine un disque specifique'''

    tour_index, hauteur, _ = position_disque(plateau, num_disque)
    disque_width = largeur_disque(num_disque)

    third_width = largeur_base(n) / 3
    third_x = third_width * tour_index
    offset = third_width / 2 - disque_width / 2

    rect(
        third_x + offset,
        (hauteur + 1) * 20,
        largeur_disque(num_disque),
        20,
        fill_color=color,
    )


def efface_disque(plateau, n, num_disque, state): 
    '''efface un disque en utilisant dessine_disque mais en blanc'''
    dessine_disque(plateau, num_disque, n, color='white')

    if state == 'single':
        for i in range(0, 3):
            dessine_tour(n, i)


def dessine_config(plateau, n): 
    '''dessine la config de depart'''
    for index_tour in range(0, len(plateau)):
        l = list(plateau[index_tour])
        for i in range(0, len(l)) :
            dessine_disque(plateau, l[i],n,'black')


def efface_tout(plateau, n): 
    for index_tour in range(0, len(plateau)):
        l = list(plateau[index_tour])
        for i in range(0, len(l)):
            efface_disque(plateau, l[i], n, 'yesai')

        goto(-300, 200)
    for i in range(0, 3):
        dessine_tour(n)
