import random

from .Box import Box


class Chance(Box):

    list_carte = []

    def __init__(self):
        pass

    def setlistcarte(cls, carte):
        Chance.list_carte = Chance.list_carte.append(carte)

    def drawlotscarte(self):
        return random.choice(Chance.list_carte)

    setlistcarte = classmethod(setlistcarte)
