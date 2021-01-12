from games.collecto.action import Action
from games.collecto.collecto import Collecto
from games.abstract_game import AbstractGame

from games.collecto.muzero_config import MuZeroConfig


class Game(AbstractGame):
    def __init__(self, seed=None):
        self.env = Collecto()

    def step(self, action):
        return self.env.step(action)

    def to_play(self):
        return self.env.to_play()

    def legal_actions(self):
        return self.env.legal_actions()

    def reset(self):
        return self.env.reset()

    def render(self):
        self.env.render()
        input("Press enter to take a step ")

    def expert_agent(self):
        return self.env.choose_random_move()

    def action_to_string(self, action_number):
        return str(Action.from_num(action_number))
