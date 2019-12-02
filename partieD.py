def dernier_coup(coups: dict, dernier_index: int) -> tuple:
    return coups[dernier_index]

def annuler_dernier_coup(coups: dict, dernier_index: int) -> tuple:
    coup = dernier_coup(coups, dernier_index)
    del coups[dernier_index]
    return coup