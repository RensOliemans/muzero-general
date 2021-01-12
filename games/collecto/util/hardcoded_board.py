import numpy as np

from games.collecto.util.consts import *


# Bord uit de spelregels gehardcode
def get_board():
    return np.array([
        [R, O, Y, P, G, B, P],
        [B, Y, B, Y, O, R, O],
        [R, P, Y, P, R, P, G],
        [B, Y, B, E, O, B, O],
        [G, B, G, Y, R, G, R],
        [O, P, Y, O, G, P, G],
        [P, R, B, R, Y, G, O]
    ])


def get_board2():
    return np.array([
        [E, E, E, E, E, E, E],
        [E, E, O, E, P, G, P],
        [O, E, E, E, E, E, E],
        [G, O, P, E, E, E, E],
        [E, E, E, E, G, E, P],
        [G, B, R, Y, E, P, O],
        [O, E, E, G, E, B, R]
    ])
