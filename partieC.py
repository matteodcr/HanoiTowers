from partieA import *
from partieB import *

def lire_coords(plateau):
	index_tour_dep = int(input('Saisir numéro tour départ'))
	index_tour_fin = int(input('Saisir numéro tour arrivée'))
	while index_tour_dep <= -1 or index_tour_dep>2 or index_tour_fin < 0 or index_tour_fin>2 or verifier_deplacement(plateau, index_tour_dep, index_tour_fin)== False :  
		index_tour_dep  = int(input('Saisir numéro tour départ'))
		index_tour_fin  = int(input('Saisir numéro tour arrivée'))

	return index_tour_dep, index_tour_fin

def jouer_un_coup(plateau, n):
	index_tour_dep, index_tour_fin = lire_coords(plateau)
	if index_tour_dep > -1 :
		efface_disque(plateau, n, disque_superieur(plateau, index_tour_dep), 'single')
		plateau[index_tour_fin].append(disque_superieur(plateau, index_tour_dep))
		del plateau[index_tour_dep][disque_superieur(plateau,index_tour_dep)+1]
		if disque_superieur(plateau, index_tour_dep) == -1:
			print(disque_superieur(plateau, index_tour_fin))
		dessine_disque(plateau, disque_superieur(plateau, index_tour_fin), n,'noir')

	else : return index_tour_dep

def boucle_jeu(plateau, n):
	limite_coup = 5
	while verifier_victoire(plateau, n) != True:
		if jouer_un_coup(plateau,n) == -1: 
			return "Vous avez decidé d'arrêter."
		if limite_coup == 0 :
			return "Perdu ! Vous avez utilisé tous les coups"
		limite_coup -= 1
	return "Vous avez gagné"










