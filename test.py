import pytest

import partieA


def test_init_plateau():
    plateau = partieA.init(3)
    
    assert plateau[0] == [3, 2, 1]
    assert plateau[1] == plateau[2] == []
    assert len(plateau) == 3


def test_nombre_disques():
    plateau = [[1, 2], [], [3]]

    assert partieA.nombre_disques(plateau, 0) == 2
    assert partieA.nombre_disques(plateau, 1) == 0
    assert partieA.nombre_disques(plateau, 2) == 1


def test_disque_superieur():
    plateau = [[], [3, 2], [4, 1]]

    assert partieA.disque_superieur(plateau, 0) == 0
    assert partieA.disque_superieur(plateau, 1) == 2
    assert partieA.disque_superieur(plateau, 2) == 1


def test_position_disque():
    plateau = [[], [1], [3, 2]]

    assert partieA.position_disque(plateau, 1) == (1, 0, 1)
    assert partieA.position_disque(plateau, 3) == (2, 0, 2)
    assert partieA.position_disque(plateau, 2) == (2, 1, 2)
    
    with pytest.raises(IndexError):
        partieA.position_disque(plateau, 4)


def test_verifier_deplacement():
    plateau = [[2, 1], [], [3]]

    assert partieA.verifier_deplacement(plateau, 0, 1) == True
    assert partieA.verifier_deplacement(plateau, 0, 2) == True
    assert partieA.verifier_deplacement(plateau, 1, 2) == False
    assert partieA.verifier_deplacement(plateau, 2, 0) == False
    assert partieA.verifier_deplacement(plateau, 0, 0) == False
