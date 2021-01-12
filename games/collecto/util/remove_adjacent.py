import numpy as np

from games.collecto.util.consts import E
from games.collecto.board import Board


def remove_adjacent(board):
    new_board = np.copy(board)
    equal_neighbours = _get_equal_neighbours(board)
    balls = []

    for x, (i, j) in equal_neighbours:
        new_board[i][j] = E
        balls.append(x)
    return new_board, balls


def _get_equal_neighbours(board):
    to_remove = set()
    for i, xs in enumerate(board):
        for j, x in enumerate(xs):
            if x == E:
                continue
            neighbours = _neighbours(board, (i, j))
            equal_neighbours = {n for n in neighbours if x == n[0]}
            if equal_neighbours:
                to_remove = to_remove | equal_neighbours
                to_remove.add((x, (i, j)))
    return to_remove


def _neighbours(board, location):
    i, j = location
    left = get_loc(board, i-1, j)
    right = get_loc(board, i+1, j)
    up = get_loc(board, i, j-1)
    down = get_loc(board, i, j+1)
    neighbours = [left, right, up, down]
    return [n for n in neighbours if n is not None and -1 not in n[1]]


def get_loc(board, i, j):
    try:
        return board[i][j], (i, j)
    except IndexError:
        return
