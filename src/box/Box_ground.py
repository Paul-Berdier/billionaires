from .Box import Box


class Ground(Box):
    def __init__(self, name, band,  price, price_band, value):
        self.name_ground = name
        self.name_band = band
        self.price_ground = price
        self.price_ground_band = price_band
        self.value_ground = value