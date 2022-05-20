from src.box import Box, Box_jail, Box_chance, Box_ground, Box_start, Box_cop, Box_lotto
from src.player import Player

class Board:

    box_number = 24
    account_loto = 0

    def __init__(self):
        self.list_box = ["start", "rue 1", "rue 2","chance", "rue 3", "rue 4",
                         "jail", "rue 5", "rue 6", "chance", "rue 7", "rue 8",
                         "lotto", "rue 9", "rue 10","chance", "rue 11", "rue 12",
                         "cop", "rue 13", "rue 14", "chance", "rue 15", "rue 16"]
        self.account_loto = Board.account_loto

    def get_account_lotto(self):
        return self.account_loto

    def set_account_lotto(self, price):
        self.account_loto =+ price

    def box_effect(self, player):
        match x:
            case 'start':
                pass
            case 'rue':
                pass
            case 'chance':
                pass
            case 'lotto':
                player.set_account()



# def init_list_box(number):
#     list_box = []
#     for i in range(number - 1):
#         if i == 3 | i == 9 | i == 15 | i == 21:
#             list_box.append(chance = Box_chance())
#         elif i == 0 | i == 6 | i == 12 | i == 18:
#             if i == 0:
#                 list_box.append(start = Box_start())
#             if i == 0:
#                list_box.append(Box_start())
#
#
#     return list_box