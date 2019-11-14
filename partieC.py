def lire_coords(plateau):
	num_tourd = int(input('Saisir numéro tour départ'))
	while num_tourd < 0 or num_tourd>2 :
		num_tourd = int(input('Erreur ! Choisir entre 0 et 2'))
	num_toura = int(input('Saisir numéro tour arrivée'))

