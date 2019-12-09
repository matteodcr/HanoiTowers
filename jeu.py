import time
from turtle import *

from partieB import *
from storage import Storage


class Jeu:

    def __init__(self, n):
        self.limite_coup = 100
        #self.compteur = 0
        self.time_start = None
        self.n = n
        self.storage = Storage()
        self.plateau = self.init(n)  # Création d'un nouvel entier: count
        self.coups_index = 0
        self.cancel = 'notcancel'
        self.coups = {}


    def init(self, n: int) -> list:
        '''Crée une liste de liste représentant le plateau initial : [[n,...,2,1],[],[]]'''

        return [list(range(n, 0, -1)), [], []]


    def nombre_disques(self, index_tour: int): 
        '''Renvoie le nombre de disques dans index_tour '''
        return len(self.plateau[index_tour])


    def disque_superieur(self, index_tour: int) -> int: 
        '''Renvoie le dernier element de la liste index_tour : le disque superieur'''

        tour = self.plateau[index_tour] # Selectionne la tour choisie

        if len(tour) == 0: return 0 
        else: return tour[len(tour) - 1]


    def position_disque(self, num_disque: int) -> tuple: 
        ''' [double boucle for] Renvoie l'index de la tour, l'index du disque et 
            la longueur de la tour'''

        # On parcours les 3 tours
        for index_tour, valeur_tour in enumerate(self.plateau):

            # On parcours les disques d'une tour
            for index_disque, valeur_disque in enumerate(valeur_tour):

                if valeur_disque == num_disque: # Si on trouve le disque recherché
                    return index_tour, index_disque, len(valeur_tour)

        raise IndexError(
            'Couldn\'t find disk {}, n={}'.format(num_disque, self.n)
        )


    def verifier_deplacement(self, index_tour_dep: int, index_tour_fin: int) -> bool:
        '''Renvoie un booléen pour savoir si un deplacement de disque sup 
        de index_tour_dep vers disque sup de index_tour_fin est possible'''

        if (index_tour_dep <= -1) or (index_tour_dep > 2) or (index_tour_fin < 0) or (index_tour_fin > 2) or (index_tour_fin == None) or (index_tour_fin == None):
            return False
        
        if self.nombre_disques(index_tour_dep) == 0:
            print("Erreur liste de depart vide")
            return False

        if self.nombre_disques(index_tour_fin) == 0:
            print("Liste d'arrivée vide")
            return True

        # On ne peut pas placer un disque plus grand sur un disque plus petit
        if self.disque_superieur(index_tour_dep) >= self.disque_superieur(index_tour_fin): 
            print('Erreur disque trop grand')
            return False

        return True


    def verifier_victoire(self) -> bool: 
        ''' Renvoie un booléen : la liste finale est elle l'inverse de la liste de départ ? '''

        copy = list(self.plateau) # Liste temporaire

        compare = self.init(self.n) 
        compare.reverse() # Liste de départ inversée : liste d'arrivée souhaitée

        if copy != compare: return False

        return True


    def dessine_disque(self, num_disque: int, color = 'black'): 
        ''' Dessine un disque specifique '''

        tour_index, hauteur, _ = self.position_disque(num_disque)
        disque_width = largeur_disque(num_disque)

        # Longueurs utilisées pour diriger la tortue
        third_width = largeur_base(self.n) / 3
        third_x = third_width * tour_index
        offset = third_width / 2 - disque_width / 2

        rect(
            third_x + offset,
            (hauteur + 1) * 20,
            largeur_disque(num_disque),
            20,
            fill_color=color,
        )


    def efface_disque(self, n, num_disque, state): 
        ''' Efface un disque en utilisant dessine_disque mais en blanc '''
        self.dessine_disque(num_disque, color='white')

        # Si on efface qu'un seul disque (hors efface_tout)
        if state == 'single':
            for i in range(0, 3):
                dessine_tour(n, i)


    def dessine_config(self): 
        ''' Dessine la configuration initiale de plateau '''
        # Première boucle pour les tours
        for index_tour in range(0, len(self.plateau)):
            l = list(self.plateau[index_tour])
            # Deuxième boucle pour les disques d'une tour [index_tour]
            for i in range(0, len(l)):
                self.dessine_disque(l[i], 'black')


    def efface_tout(self):
        ''' Efface tous les disques du plateau '''
        for index_tour in range(0, len(self.plateau)):
            l = list(self.plateau[index_tour])
            for i in range(0, len(l)):
                self.efface_disque(l[i], 'yesai')
        for i in range(0, 3):
            dessine_tour(self.n)


    def lire_coords(self) -> tuple:
        '''[pas utilisé]
            trie les numéro de tour de dep. et d'arrivée pour qu'elle remplisse les conditions'''

        index_tour_dep = -2
        index_tour_fin = -2

        while (index_tour_dep <= -1) or (index_tour_dep > 2) or (index_tour_fin < 0) or (index_tour_fin > 2) or self.verifier_deplacement(index_tour_dep, index_tour_fin) == False:  
            index_tour_dep  = int(input("Saisir numéro tour départ : "))
            index_tour_fin  = int(input("Saisir numéro tour arrivée : "))

        return index_tour_dep, index_tour_fin


    def changer_disque_tour(self, index_tour_dep, index_tour_fin):
        ''' Modifie la liste et archive l'historique des configurations de plateau dans le dico '''
        if self.cancel == 'notcancel' :
            
            self.coups_index += 1 # Ajoute un point au compteur
            self.coups[self.coups_index] = (index_tour_dep, index_tour_fin)

        self.plateau[index_tour_fin].append(self.disque_superieur(index_tour_dep))
        del self.plateau[index_tour_dep][-1]


    def jouer_un_coup(self, index_tour_dep, index_tour_fin) -> tuple:
        ''' Transfere un disque d'une tour a l'autre, en dessin et sur la liste '''

        if self.time_start == None:
            self.time_start = time.time()

        print(self.coups)
        if index_tour_dep != -1:
            self.efface_disque(self.n, self.disque_superieur(index_tour_dep), 'single')
            self.changer_disque_tour(index_tour_dep, index_tour_fin)
            self.dessine_disque(self.disque_superieur(index_tour_fin), 'black') 

            won = self.verifier_victoire()

            return won, ("Gagné" if won else "PERDU")

        if self.coups_index == self.limite_coup:
            return True, "Limite de coup atteinte"   

        else:
            return True, "Vous avez décidé d'arrêter"


    def dernier_coup(self, coups: dict, dernier_index: int) -> tuple:
        return self.coups[self.coups_index]


    def annuler_dernier_coup(self, coups: dict, dernier_index: int) -> tuple:
        self.cancel = 'cancel'
        coup = self.dernier_coup(self.coups, self.coups_index)
        self.jouer_un_coup(coup[1], coup[0])
        del self.coups[self.coups_index]
        self.coups_index -= 1 # Ajoute un point au compteur
        self.cancel = 'notcancel'
        return coup
