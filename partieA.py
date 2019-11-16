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
    else: return tour[len(tour)-1]

def position_disque(plateau: list, numdisque):
    for index_tour,value_tour in enumerate(plateau):
        l = list(plateau[index_tour])
        for i in range(0,len(l)) :
            if l[i]-1 == numdisque :
                return index_tour, l[i], len(l)+1
    return None


def verifier_deplacement(plateau, nt1, nt2):
    if nombre_disques(plateau, nt2)==0:
        print("liste d'arrivée vide")
        return True
    if nombre_disques(plateau,nt1)==0 :
        print("Erreur liste de depart vide")
        return False
    if disque_superieur(plateau, nt1)>disque_superieur(plateau, nt2) : 
        print('Erreur disque trop grand')
        return False
    return True
 
def verifier_victoire(plateau,n):
    copy = list(plateau)
    compare = init(n)
    compare.reverse()
    if copy != compare : return False
    return True




