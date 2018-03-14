def convert_ltr_coord(coord):
    """
    (string) -> (int)
    This function converts coordinate letter to it's index so it can be used as
    a list index.
    >>> convert_ltr_coord("A")
    0
    >>> convert_ltr_coord("D")
    3
    """
    letters = "ABCDEFGHIJ"
    return letters.index(coord)


def ship_size(data, coords_tuple):
    """-
    (data, tuple) -> (tuple)
    This functions returns a ship size.
    For example, (J, 1) or (A, 10)
    """
    i_0 = convert_ltr_coord(coords_tuple[0])
    j_0 = coords_tuple[1]-1
    lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    counter = 1
    for i, j in lst:
        crd1 = i
        crd2 = j
        try:
            while data[i_0+i][j_0+j] != " ":
                i += crd1
                j += crd2
                counter += 1
        except:
            pass
    return counter


def is_valid(data):
    """
    (data) -> (bool)
    This function checks if the given field is valid for the Battleship game.
    >>> is_valid([[1], [1,2], [23], [34]])
    False
    """
    def check_ship_position(matrix):
        """
        (list) -> (bool)
        This function checks if the situation of ships is valid
        according to the Battleship rules.
        """
        lst = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        lenn = len(matrix)
        for i in range(lenn):
            for j in range(lenn):
                if matrix[i][j] != " ":
                    for x, y in lst:
                        try:
                            if matrix[i + x][j + y] in ("O", "X"):
                                return False
                        except:
                            pass
        return True

    def check_ships_amount(matrix):
        """
        (list) -> (bool)
        This function checks if there is exact amount of ships is true.
        """
        needed_ships = {1: 4, 2: 3, 3: 2, 4: 1}
        ships = {1: 0, 2: 0, 3: 0, 4: 0}
        letters = "ABCDEFGHIJ"
        lenn = len(matrix)
        for i in range(lenn):
            for j in range(lenn):
                if matrix[i][j] != " ":
                    curr_ship = ship_size(matrix, (letters[i], j+1))
                    if curr_ship == 1:
                        ships[1] += 1
                    elif curr_ship == 2:
                        ships[2] += 1
                    elif curr_ship == 3:
                        ships[3] += 1
                    elif curr_ship == 4:
                        ships[4] += 1
                    else:
                        return False
        for i in ships.keys():
            ships[i] /= i
        if ships == needed_ships:
            return True
        else:
            return False
    if sum(len(item) for item in data) != 100:
        return False
    if check_ship_position(data) == False:
        return False
    if check_ships_amount(data) == False:
        return False
    return True


def field_to_str(data):
    """
    (data) -> (str)
    This function converts a field in list of lists to string format.
    """
    line = "      *************************************************************\n"
    nums_str = "          1     2     3     4     5     6     7     8     9    10\n"
    field_str = ""+nums_str+line
    letters = "ABCDEFGHIJ"
    for i in range(len(data)):
        field_str += "   "+letters[i]+"  |"
        for j in range(len(data[i])):
            field_str += "  "+data[i][j]+"  |"
        field_str += "\n"
        field_str += line
    return field_str