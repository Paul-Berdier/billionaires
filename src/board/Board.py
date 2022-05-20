from src.box import Box, Box_jail, Box_chance, Box_ground, Box_start, Box_cop, Box_lotto

class Board:

    box_number = 24
    account_loto = 0

    def __init__(self):
        self.list_box = []
        self.account_loto = Board.account_loto

def init_list_box(number):
    list_box = []
    for i in range(number - 1):
        if i == 3 | i == 9 | i == 15 | i == 21:
            list_box.append(chance = Box_chance())
        elif i == 0 | i == 6 | i == 12 | i == 18:
            if i == 0:
                list_box.append(start = Box_start())
            if i == 0:
                list_box.append(Box_start())


    return list_box