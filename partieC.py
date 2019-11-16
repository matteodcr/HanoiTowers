from partieA import *
from partieB import *

def lire_coords(plateau):
	ntd = int(input('Saisir numéro tour départ'))
	nta = int(input('Saisir numéro tour arrivée'))
	while ntd <= -1 or ntd>2 or nta < 0 or nta>2 or verifier_deplacement(plateau, ntd, nta)== False :  
		ntd = int(input('Saisir numéro tour départ'))
		nta = int(input('Saisir numéro tour arrivée'))

	return ntd, nta

def jouer_un_coup(tableau, n):
	num_tourd, num_toura = lire_coords(tableau)
	if num_tourd > -1 :
		efface_disque(plateau, num_tourd, n)
		dessine_disque(plateau, num_toura, n,'noir')

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

def main_test(n):
	plateau = [[1],[3],[2]]
	print(lire_coords(plateau))


main_test(3)





