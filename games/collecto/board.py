import random
import numpy as np
from games.collecto.util.consts import *
from games.collecto.util.hardcoded_board import get_board


class Board:
    def __init__(self, board=None):
        self.board = np.array([[E] * 7] * 7, dtype='object') if board is None else board

    def copy_board(self, b):
        self.board = np.array(b).copy()

    def add_random_balls(self, amount):
        if amount > 48:
            raise Exception('Amount must be smaller than 49')
        for _ in range(amount):
            colour = random.choice(COLOURS)
            t = tuple(random.choice(np.argwhere(np.array([[x == E for x in row] for row in self.board]))))
            self.add_ball(colour, t)

    def add_balls(self, ball_list):
        for ball in ball_list:
            colour = ball[0]
            coordinate = ball[1:]
            self.add_ball(colour, coordinate)

    def add_ball(self, colour, coordinate):
        self.board[coordinate] = colour

    def get_position(self, coordinate):
        return self.board[coordinate].colour if not self.position_is_empty(coordinate) else E

    def position_is_empty(self, coordinate):
        return self.board[coordinate] == E

    def position_is_colour(self, colour, coordinate):
        return self.board[coordinate].colour == colour if not self.position_is_empty(coordinate) else False

    def __eq__(self, other):
        for i, elem in enumerate(self.board):
            for j, elem2 in enumerate(elem):
                if elem2 != other.board[i][j]:
                    return False
        return True

    def __repr__(self):
        line = " "
        line += " ---" * 7
        print("   0   1   2   3   4   5   6")
        for i, row in enumerate(self.board):
            print(line)
            ve = str(i)
            for place in row:
                if place == E:
                    ve += "|   "
                else:
                    ve += "| " + place.get_cap() + " "
            ve += "|"
            print(ve)
        print(line)


if __name__ == '__main__':
    b = Board()
    b.copy_board(get_board())
    # b.add_random_balls(30)
    b.__repr__()
