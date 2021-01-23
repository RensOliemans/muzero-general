import numpy as np
import time

from games.collecto.util.consts import *
from games.collecto.util.remove_adjacent import _get_equal_neighbours


def get_board(random):
    return get_random_board() if random else get_static_board()


def get_static_board():
    return np.array([
        [R, O, Y, P, G, B, P],
        [B, Y, B, Y, O, R, O],
        [R, P, Y, P, R, P, G],
        [B, Y, B, E, O, B, O],
        [G, B, G, Y, R, G, R],
        [O, P, Y, O, G, P, G],
        [P, R, B, R, Y, G, O]
    ])


def get_random_board():
    orig_balls = np.array([colour for colour in COLOURS*8])
    valid = False
    while not valid:
        balls = np.copy(orig_balls)
        print('Creating random board')
        np.random.shuffle(balls)
        balls = np.insert(balls, 24, E)
        balls = np.reshape(balls, (-1, 7))

        print(balls)
        print(_get_equal_neighbours(balls))
        time.sleep(10)
        valid = len(_get_equal_neighbours(balls)) == 0

    return balls
