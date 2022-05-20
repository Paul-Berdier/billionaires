from .Box import Box


class Jail(Box):
    def __init__(self):
        self.contain_player = []

    def add_player(self, player):
        self.contain_player.append(player)

    def del_player(self, player):
        self.contain_player.remove(player)

    def get_player(self):
        return self.contain_player
