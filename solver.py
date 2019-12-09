from jeu import Jeu


class Solver:

    def __init__(self, game):
        self.game = game

    def get_steps(self, n=None, src=0, aux=1, dest=2) -> iter:
        if n is None:
            n = self.game.n

        if n == 1:
            yield (src, dest)
        else:
            yield from self.get_steps(n-1, src, dest, aux)
            yield (src, dest)
            yield from self.get_steps(n-1, aux, src, dest)
