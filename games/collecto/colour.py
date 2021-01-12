class Colour:
    def __init__(self, colour):
        self.colour = colour

    @property
    def cap(self):
        return self.colour[0].capitalize()

    def __repr__(self):
        return self.cap

    def __str__(self):
        return self.cap

    def __eq__(self, other):
        return self.colour == other.colour

    def __hash__(self):
        return hash(self.colour)
