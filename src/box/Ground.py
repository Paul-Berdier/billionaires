from .Box import Box


class Ground(Box):
    def __init__(self, name, band, price, value):
        self.name_ground = name
        self.name_band = band
        self.price_ground = price
        self.value_ground = value