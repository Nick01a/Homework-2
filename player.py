from field import Field

class Player():
    def __init__(self, name):
        """
        This method initializes a new Player instance.
        """
        self.__name = name

    def read_position(self):
        """
        This method asks Player for the coord to shoot at, reads it from input
        and returns it as a tuple
        """
        print(self.__name + " enter move: ")
        x, y = input().split()
        return x, int(y)
