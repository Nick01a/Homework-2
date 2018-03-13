class Ship():
    def __init__(self, bow, horizontal, length):
        """
        This method initializes an instance of Ship class.
        :param bow: (tuple) start coord of the ship
        :param horizontal: (bool) - if ship situated horizontal
        :param length: (int) - length of the ship
        """
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = [False] * length  # lst of bool if ship's part id damaged

    def shoot_at(self, crd):
        """
        This method takes a coord of ship and makes it damaged.
        :param crd: coord that was shooten at
        :return: None
        """
        if self.__length:
            self.__hit[abs(crd[0] + crd[1] - self.bow[0] - self.bow[1])] = True
        else:
            self.__hit = [True]