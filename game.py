from field import Field
from player import Player


class Game():
    def __init__(self):
        """
        This method initializes a Game class.
        field: - list of Fields for the game
        players: - list of Players for the game
        """
        field1, field2 = Field(), Field()
        self.__field = [field1, field2]
        name1 = str(input("Please enter name:"))
        name2 = str(input("Please enter name:"))
        self.__players = [Player(name1), Player(name2)]
        self.__current_player = 1

    def read_position(self):
        """
        This method asks current player to shoot and change a field.
        """
        if self.__current_player == 1:
            coord = self.__players[0].read_position()
            self.__field[1].shoot_at(coord)
            self.__current_player = 2
        else:
            coord = self.__players[1].read_position()
            self.__field[0].shoot_at(coord)
            self.__current_player = 1

    def field_without_ships(self):
        """
        This method display a field in string
        """
        if self.__current_player == 1:
            return self.__field[1].field_without_ships()
        return self.__field[0].field_without_ships()

    def field_with_ships(self):
        """
        This method display a field in string with elements (ships).
        """
        if self.__current_player == 1:
            return self.__field[0].field_with_ships()
        return self.__field[1].field_with_ships()