from partieA import *
from partieB import *


def changer_disque_tour(plateau, index_tour_dep, index_tour_fin):
	plateau[index_tour_fin].append(disque_superieur(plateau, index_tour_dep))
	del plateau[index_tour_dep][-1]

def lire_coords(plateau):
	'''trie les numéro de tour de dep. et d'arrivée pour qu'elle remplisse les conditions'''

	index_tour_dep = -2
	index_tour_fin = -2

	while index_tour_dep <= -1 or index_tour_dep>2 or index_tour_fin < 0 or index_tour_fin>2 or verifier_deplacement(plateau, index_tour_dep, index_tour_fin)== False :  
		index_tour_dep  = int(input("Saisir numéro tour départ : "))
		index_tour_fin  = int(input("Saisir numéro tour arrivée : "))

	return index_tour_dep, index_tour_fin

def jouer_un_coup(plateau, n):
	'''transfere un disque d'une tour a l'autre, en dessin et sur la liste'''

	index_tour_dep, index_tour_fin = lire_coords(plateau)

	if index_tour_dep != -1 :
		efface_disque(plateau, n, disque_superieur(plateau, index_tour_dep), 'single')
		# if disque_superieur(plateau, index_tour_dep) == -1:
		# 	print(disque_superieur(plateau, index_tour_fin))
		changer_disque_tour(plateau, index_tour_dep,index_tour_fin)
		dessine_disque(plateau, disque_superieur(plateau, index_tour_fin), n, 'black')
		return index_tour_dep

	else : return index_tour_dep

def boucle_jeu(plateau, n):
	'''boucle de jeu qui se coupe selon les conditions données ...'''
	limite_coup = 5
	while not verifier_victoire(plateau, n):
		arret = jouer_un_coup(plateau,n)
		print(plateau)
		if arret == -1: 
			return "Vous avez decidé d'arrêter."
		if limite_coup == 0 :
			return "Perdu ! Vous avez utilisé tous les coups"
		limite_coup -= 1
	return "Vous avez gagné"
