from partieA import *
from partieB import *

def lire_coords(plateau):
	ntd = int(input('Saisir numéro tour départ'))
	nta = int(input('Saisir numéro tour arrivée'))
	while ntd < 0 or ntd>2 or nta < 0 or nta>2 or not verifier_deplacement(plateau, nta, ntd):  
		ntd = int(input('Saisir numéro tour départ'))
		nta = int(input('Saisir numéro tour arrivée'))

	return ntd, nta

def jouer_un_coup(tableau, n):
	num_tourd, num_toura = lire_coords(tableau)
	efface_disque(plateau, num_tourd, n)
	dessine_disque(plateau, num_toura, n,'noir')

def boucle_jeu(plateau, n):
	while verifier_victoire(plateau, n) != True :
		jouer_un_coup(tableau,n)

