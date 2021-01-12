import numpy as np

from games.collecto.util.consts import *


# Bord uit de spelregels gehardcode
def get_board():
    return np.array([
        [Y, P, B, E, E, B, R],
        [E, E, O, E, P, G, P],
        [O, E, E, E, E, E, E],
        [G, O, P, E, E, E, E],
        [E, E, E, E, G, E, P],
        [G, B, R, Y, E, P, O],
        [O, E, E, G, E, B, R]
    ])
