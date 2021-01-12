class Colour:
    def __init__(self, colour):
        self.colour = colour

    def get_cap(self):
        return self.colour[0].capitalize()

    def __eq__(self, other):
        return self.colour == other.colour
