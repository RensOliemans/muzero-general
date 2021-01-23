from games.collecto.collecto import Collecto
from games.aml_collecto import Game as StaticGame

from games.collecto.muzero_config import MuZeroConfig


class Game(StaticGame):
    def __init__(self, seed=None):
        self.env = Collecto(random=True)

