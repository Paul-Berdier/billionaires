from .Box import Box


class Jail(Box):
    def __init__(self, type="jail"):
        Box.__init__(self, type)
