from enum import Enum, auto


class Action:
    def __init__(self, direction, index: int):
        self.direction = direction
        self.index = index

    def to_num(self):
        return self.index + (self.direction.value - 1) * 7

    @classmethod
    def from_num(cls, num):
        return Action(Direction(num // 7 + 1), num % 7)

    def __eq__(self, other):
        return self.direction == other.direction and self.index == other.index

    def __repr__(self):
        return f"<Action. Direction: {self.direction.name}, Index: {self.index}"


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


def transpose_direction(direction):
    if direction is Direction.UP:
        return Direction.LEFT
    elif direction is Direction.DOWN:
        return Direction.RIGHT


def convert_direction(s):
    s = s.lower()
    if s == 'l' or s == 'left':
        return Direction.LEFT
    elif s == 'r' or s == 'right':
        return Direction.RIGHT
    elif s == 'u' or s == 'up':
        return Direction.UP
    elif s == 'd' or s == 'down':
        return Direction.DOWN