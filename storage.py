import pickle
import time


class Storage:

    def __init__(self, filename = "scores.bin"):
        self.filename = filename

    def read_scores(self):
        ''' Ouvre le fichier '''
        # On essaie d'ouvrir le fichier, si ca ne marche pas on retourne une liste vide
        try:
            file = open(self.filename, "rb")
            return pickle.load(file)
        except:
            return []

    def write_scores(self, scores: list):
        ''' Rajoute des scores au fichier '''
        file = open(self.filename, "wb+")
        pickle.dump(scores, file)

    def append_score(self, name: str, nb_disks: int, nb_moves: int, game_length: float):
        ''' Récolte toutes les données qui vont être rajoutées au fichier des scores '''
        now = time.time() 
        score = (name, nb_disks, nb_moves, now)
        
        # On met à jour le fichier grace auux fonctions précédentes
        scores = self.read_scores()
        scores.append(score)
        self.write_scores(scores)

    def get_scores_sorted(self, count = 5):
        ''' Classe les scores en fonction du nombre de coups '''
        scores = self.read_scores()
        scores_sorted = sorted(scores, key=lambda score: score[2])
        return scores_sorted[:count]
