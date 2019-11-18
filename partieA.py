def init(n) : #ok
    '''Crée une liste de liste représentant le plateau initial : [[n,...,2,1],[],[]]'''

    plateau = []             
    TourInit = []          
    TourIntermediaire = []
    TourDestination = []   
  
    for i in range(n,0,-1):
        TourInit.append(i)

    plateau.append(TourInit)
    plateau.append(TourIntermediaire)
    plateau.append(TourDestination)

    return plateau

def nombre_disques(plateau:list, IndexTour): #ok
    '''Renvoie le nombre de disques dans IndexTour'''
    return len(plateau[IndexTour])

def disque_superieur(plateau: list, IndexTour): #ok
    '''Renvoie le dernier element de la liste IndexTour : le disque superieur'''

    tour = plateau[IndexTour]
    if len(tour) == 0: return -1
    else: return tour[len(tour)-1]

def position_disque(plateau: list, NumDisque): #ok
    '''Renvoie la position d'un disque'''

    for index_tour in range(0,len(plateau)):
        if len(plateau[index_tour]) == 0 :
            return -1, -1, 0
        l = list(plateau[index_tour])
        for i in range(0,len(l)) :
            if l[i] == NumDisque :
                return index_tour, i, len(l)

    return 'error'

def verifier_deplacement(plateau:list, index_tour_dep, index_tour_fin): #ok
    '''Renvoie un booléen pour savoir si un deplacement de disque sup 
       de index_tour_dep vers disque sup de index_tour_fin est possible'''

    if nombre_disques(plateau,index_tour_dep)==0 :
        print("Erreur liste de depart vide")
        return False

    if nombre_disques(plateau,index_tour_fin)==0 :
        print("Liste d'arrivée vide")
        return True

    if disque_superieur(plateau, index_tour_dep)>disque_superieur(plateau, index_tour_fin) : 
        print('Erreur disque trop grand')
        return False

    return True
 
def verifier_victoire(plateau:list, n): #ok
    '''Renvoie un booléen : la liste finale est elle l'inverse de la liste de départ ?'''

    copy = list(plateau)
    compare = init(n)
    compare.reverse()
    if copy != compare : return False

    return True