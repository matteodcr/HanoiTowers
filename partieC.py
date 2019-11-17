from partieA import *
from partieB import *

def lire_coords(plateau):
	IndexTourDep = int(input('Saisir numéro tour départ'))
	IndexTourFin = int(input('Saisir numéro tour arrivée'))
	while ntd <= -1 or ntd>2 or nta < 0 or nta>2 or verifier_deplacement(plateau, ntd, nta)== False :  
		IndexTourDep  = int(input('Saisir numéro tour départ'))
		IndexTourFin  = int(input('Saisir numéro tour arrivée'))

	return IndexTourDep, IndexTourFin

def jouer_un_coup(plateau, n):
	IndexTourDep, IndexTourFin = lire_coords(plateau)
	if IndexTourDep > -1 :
		efface_disque(plateau, disque_superieur(plateau, IndexTourDep)-1, n, 'single')
		plateau[num_toura].append(disque_superieur(plateau, num_tourd))
		del plateau[num_tourd][disque_superieur(plateau,num_tourd)+1]
		if disque_superieur(plateau, num_tourd) == '-1'
		print(disque_superieur(plateau, num_toura))
		dessine_disque(plateau, disque_superieur(plateau, IndexTour), n,'noir')

	else : return num_tourd

def boucle_jeu(plateau, n):
	limite_coup = 5
	while verifier_victoire(plateau, n) != True:
		if jouer_un_coup(plateau,n) == -1: 
			return "Vous avez decidé d'arrêter."
		if limite_coup == 0 :
			return "Perdu ! Vous avez utilisé tous les coups"
		limite_coup -= 1
	return "Vous avez gagné"










