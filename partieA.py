def init(n) -> list: 
    '''Crée une liste de liste représentant le plateau initial : [[n,...,2,1],[],[]]'''

    # Crée la liste qui représente le plateau
    plateau = []             

    # Crée les listes qui correspondent au tours
    tour_init = []          
    tour_intermediaire = []
    tour_destination = []

    # Remplit la 1ere tour de n disques
    for i in range(n, 0, -1):
        tour_init.append(i)

    # Ajoute au plateau les 3 tours à l'état initial
    plateau.append(tour_init)
    plateau.append(tour_intermediaire)
    plateau.append(tour_destination)

    return plateau









