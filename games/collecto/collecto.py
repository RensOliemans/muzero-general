import random
from itertools import groupby

import numpy as np

from games.collecto.action import Action, Direction
from games.collecto.util.hardcoded_board import get_board
from games.collecto.util.consts import *
from games.collecto.util.exceptions import InvalidMoveException
from games.collecto.util.remove_adjacent import remove_adjacent
from games.collecto.util.shove import shove_board


class Collecto:
    def __init__(self):
        self.board = get_board()
        self.player = 1
        self._balls_of_players = {1: [], -1: []}

    def to_play(self):
        return 0 if self.player == 1 else 1

    def reset(self):
        self.board = get_board()
        self.player = 1
        self._balls_of_players = {1: [], -1: []}
        return self.get_observation()

    def step(self, action):
        self.board, balls = self._do_action(self.board, Action.from_num(action))
        self._balls_of_players[self.player].extend(balls)

        done = self.have_winner() or len(self.legal_actions()) == 0
        reward = 1 if self.have_winner() else 0

        self.player *= -1

        return self.get_observation(), reward, done

    def get_observation(self):
        """
        Returns the board in the shape of the observation: 7 channels, 1 per color each,
        and 1 for indicating whose turn it is
        """
        purple = np.where(self.board == P, 1, 0)
        orange = np.where(self.board == O, 1, 0)
        green = np.where(self.board == G, 1, 0)
        red = np.where(self.board == R, 1, 0)
        blue = np.where(self.board == B, 1, 0)
        yellow = np.where(self.board == Y, 1, 0)
        turn = np.full((7, 7), self.player)
        return np.array([purple, orange, green, red, blue, yellow, turn])

    def legal_actions(self):
        legal_actions = list()
        for i, _ in enumerate(self.board):
            for direction in Direction:
                action = Action(direction, i)
                try:
                    _, balls = self._do_action(np.copy(self.board), action)
                except InvalidMoveException:
                    continue
                if balls:
                    legal_actions.append(action.to_num())
        return legal_actions

    def have_winner(self):
        return len(self.legal_actions()) == 0 and self.is_winner()

    def is_winner(self):
        return self.player == self._calculate_winner()

    def _calculate_winner(self):
        points = {}
        for player in self._balls_of_players.keys():
            balls = self._balls_of_players[player]
            groups = groupby(sorted(balls))
            points[player] = sum([len(list(b)) // 3 for _, b in groups])
        return max(points, key=lambda x: points[x])

    def render(self):
        print(self.board)

    def choose_random_move(self):
        return random.choice(self.legal_actions())

    @staticmethod
    def _do_action(board, action):
        new_board = shove_board(board, action)
        return remove_adjacent(new_board)
