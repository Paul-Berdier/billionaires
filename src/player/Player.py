import random


class Player:

    base_account = 500
    min_dice = 1
    max_dice = 6

    def __init__(self, name):
        self.account = Player.base_account
        self.name = name
        self.last_number_dice = 0
        self.ground_list = []

    def roll(self):
        self.last_number_dice = random.randint(Player.min_dice, Player.max_dice)

    def get_last_number_dice(self):
        return self.last_number_dice

    def set_account(self, price):
        self.account =+ price

    def get_account(self):
        return self.account

    def add_ground(self):
        pass

    def del_ground(self):
        pass