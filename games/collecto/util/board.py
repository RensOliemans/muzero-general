import numpy as np

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
    balls = np.array([colour for colour in COLOURS*8])
    np.random.shuffle(balls)
    balls = np.insert(balls, 24, E)
    balls = np.reshape(balls, (-1, 7))

    equal_neighbours = _get_equal_neighbours(balls)
    while not len(equal_neighbours) == 0:
        loc = np.random.choice([i for i in range(48) if not i == 24])
        x, y = loc // 7, loc % 7
        dx, dy = equal_neighbours.pop()[1]
        balls[dx][dy], balls[x][y] = balls[x][y], balls[dx][dy]
        equal_neighbours = _get_equal_neighbours(balls)
    return balls
