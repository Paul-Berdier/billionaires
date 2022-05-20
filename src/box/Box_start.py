from .Box import Box

class Box_start(Box):

    cash = 200

    def __init__(self):
        pass

    def get_cash(self):
        return Box_start.cash