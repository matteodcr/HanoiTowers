

def init(n) :
    plateau = []             #liste des 3 tours
    tour_init = []          #liste de départ
    tour_intermediaire = []
    tour_destination = []   #tours du milieu et de gauche
  
    for i in range(n,0,-1):
        tour_init.append(i)

    plateau.append(tour_init)
    plateau.append(tour_intermediaire)
    plateau.append(tour_destination)

    return plateau

def nombre_disques(plateau: list, numtour):
    return len(plateau[numtour])

def disque_superieur(plateau: list, numtour):
    tour = plateau[numtour]
    if len(tour) == 0: return -1
    else: return tour[len(tour) - 1]

def position_disque(plateau: list, numdisque):
    for index_tour,value_tour in enumerate(plateau):
        l = list(plateau[index_tour])
        for i in range(0,len(l)) :
            if l[i]-1 == numdisque :
                return index_tour, l[i], len(l)+1


def verifier_deplacement(plateau, nt1, nt2):
    assert nombre_disques(plateau,nt1)==0
    assert disque_superieur(plateau, nt1)>(plateau, nt2)
    return True

def verifier_victoire(plateau,n):
    copy = list(plateau)
    copy.reverse()
    assert copy != plateau