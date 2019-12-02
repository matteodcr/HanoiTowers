import pickle
import time


class Storage:

    def __init__(self, filename = "scores.bin"):
        self.filename = filename

    def read_scores(self):
        try:
            file = open(self.filename, "rb")
            return pickle.load(file)
        except:
            return []

    def write_scores(self, scores: list):
        file = open(self.filename, "wb+")
        pickle.dump(scores, file)

    def append_score(self, name: str, nb_disks: int, nb_moves: int, game_length: float):
        now = time.time()
        score = (name, nb_disks, nb_moves, now)
        scores = self.read_scores()
        scores.append(score)
        self.write_scores(scores)

    def get_scores_sorted(self, count = 5):
        scores = self.read_scores()
        scores_sorted = sorted(scores, key=lambda score: score[2])
        return scores_sorted[:count]
