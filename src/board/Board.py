from src.box import Box, Box_jail, Box_chance, Box_ground, Box_start, Box_cop, Box_lotto
from src.player import Player

class Board:

    box_number = 24
    account_loto = 0

    def __init__(self):
        self.list_box = [
                        #"start", "rue 1", "rue 2","chance 1", "rue 3", "rue 4",
                         #"jail", "rue 5", "rue 6", "chance 2", "rue 7", "rue 8",
                         #"lotto", "rue 9", "rue 10","chance 3", "rue 11", "rue 12",
                         #"cop", "rue 13", "rue 14", "chance 3", "rue 15", "rue 16"
                        ]
        self.list_player = []
        self.account_loto = Board.account_loto

    def get_account_lotto(self):
        return self.account_loto

    def set_account_lotto(self, price):
        self.account_loto =+ price

    def set_list_box(self, box):
        self.list_box.append(box)

    def set_list_player(self, player):
        self.list_player.append(player)

    def box_effect(self, player):
        x = player.type_place
        match x:
            case 'start':
                pass
            case 'street':
                i = 0
                for box in self.list_box:
                    if isinstance(box, Box_ground):
                        if box.owner_name:
                            #SI LE TERRAIN APPARTIENT DEJA A QQUN
                            owner_name_box = box.owner_name
                            if player.name == box.player:
                                #AU JOUEUR QUI JOUE
                                print("Vous êtes sur un de vos terrains\n")
                            else :
                                #A UN AUTRE JOUEUR
                                for player_of_list in self.list_player:
                                    if player_of_list.name == owner_name_box:
                                        other_player = player_of_list
                                print("Vous payez {} à {}\n".format(box.price_ground, box.owner_name))
                                player.set_account(-(box.price_ground))
                                other_player.set_account(box.priceground)

                        else :
                            #DEMANDE D'ACHAT
                            dmd = string(input("Voulez vous acheter {} pour {} ? (O/N)\n").format(box.name,box.price))
                            if dmd == ("O" | "o"):
                                player.set_account(-(box.price))
                            elif dmd == ("N" | "n"):
                                pass


            case 'chance':
                #LE JOUEUR TIRE UNE CARTE CHANCE
                #a finir
                player.draw_carte()

            case 'lotto':
                #LE JOUEUR REMPORTE LE LOTO
                player.set_account(self.account_loto)
                self.account_loto = 0
            case 'cop':
                #LE JOUEUR VA EN PRISON
                player.type_place = 'jail'
                player.in_jail = True
            case 'jail':
                pass

    def move_player(self, player):
        #a finir
        pass
