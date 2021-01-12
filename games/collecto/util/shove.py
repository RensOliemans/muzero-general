import numpy as np

from games.collecto.action import Direction, transpose_direction
from games.collecto.util.consts import E
from games.collecto.util.exceptions import InvalidMoveException


def shove_board(board, action):
    if action.direction is Direction.LEFT or action.direction is Direction.RIGHT:
        row = board[action.index]
        board[action.index] = shove(row, action.direction)
    else:
        board = np.transpose(board)
        transposed_direction = transpose_direction(action.direction)
        row = board[action.index]
        board[action.index] = shove(row, transposed_direction)
        board = np.transpose(board)
    return board


def shove(row, direction):
    """Shoves the elements in a row to the left"""
    result = np.copy(row)
    empty_indices = [i for i, elem in enumerate(result) if elem == E]
    if len(empty_indices) == 0:
        raise InvalidMoveException("Cannot shove a row that has no empty spaces")

    for i, elem in enumerate(row):
        if elem == E:
            continue

        if direction == Direction.LEFT:
            # spots_to_move is the amount of 'spots' the current ball must move
            # (determined by the amount of empty cells to the (in this case) left)
            spots_to_move = len([empty_index for empty_index in empty_indices if i > empty_index])
            result[i - spots_to_move] = elem
        else:
            spots_to_move = len([empty_index for empty_index in empty_indices if i < empty_index])
            result[i + spots_to_move] = elem

    amount_of_empty = len(empty_indices)
    if direction == Direction.LEFT:
        result[-amount_of_empty:] = [E] * amount_of_empty
    else:
        result[:amount_of_empty] = [E] * amount_of_empty
    return result
