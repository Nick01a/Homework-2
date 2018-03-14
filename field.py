from ship import Ship
from main_func import convert_ltr_coord, is_valid, field_to_str
import random
#

class Field():
    def __init__(self):
        """
        This method initialize a new Field class instance.
        """
        def generate_field():
            """
            (None) -> (data)
            This function randomly generates field.
            """

            def generate_angle():
                """
                (None) -> (str)
                This function randomly generates a ship angle situation:
                vertical - "ver"
                horizontal - "hor"
                """
                if random.choice((0, 1)) == 0:
                    return "hor"
                return "ver"

            def situate_ship(ship_size, free_cells, func_field, func_oo_field):
                """
                (int), (list), (list) -> (list), (list)
                Function returns modified list of available cells and
                a modified field.
                """
                angle = generate_angle()
                ls1 = list(filter(lambda i: i[0] < 11 - ship_size, free_cells))
                ls2 = list(filter(lambda i: i[1] < 11 - ship_size, free_cells))
                if angle == "ver":
                    free_cells = ls1
                else:
                    free_cells = ls2
                if free_cells == False:
                    return free_cells, func_field, func_oo_field
                random_coord = random.choice(free_cells)
                if angle == "ver":
                    for crd1 in [-1, 0, 1]:
                        for crd2 in range(-1, ship_size + 1):
                            try:
                                free_cells.remove((random_coord[0] + crd2,
                                                   random_coord[1] + crd1))
                            except:
                                pass
                    for i in range(ship_size):
                        func_field[random_coord[0] + i][random_coord[1]] = "O"
                        new_ship = Ship(random_coord, False, ship_size)
                        func_oo_field[random_coord[0]+i][random_coord[1]] = new_ship

                if angle == "hor":
                    for crd1 in [-1, 0, 1]:
                        for crd2 in range(-1, ship_size + 1):
                            try:
                                free_cells.remove((random_coord[0] + crd1,
                                                   random_coord[1] + crd2))
                            except:
                                pass
                    for i in range(ship_size):
                        func_field[random_coord[0]][random_coord[1] + i] = "O"
                        new_sh = Ship(random_coord, True, ship_size)
                        func_oo_field[random_coord[0]][random_coord[1] + i] = \
                            new_sh
                return [free_cells, func_field, func_oo_field]

            while True:
                available_cells = [(i, j) for j in range(10) for i in range(10)]
                field = [[" " for j in range(10)] for i in range(10)]
                n_field = [[Ship((r, c), True, 0) for c in range(10)]
                            for r in range(10)]
                for num in range(1, 5):
                    if num == 1:
                        after_ship = situate_ship(1, available_cells,
                                                  field, n_field)
                        available_cells, field, n_field = after_ship[0],\
                                                           after_ship[1],\
                                                           after_ship[2]
                    for times in range(5 - num):
                        after_ship = situate_ship(num, available_cells,
                                                  field, n_field)
                        available_cells, field, on_field = after_ship[0], after_ship[1], after_ship[2]

                if is_valid(field):
                    return field, n_field
        fields = generate_field()
        self.ships = fields[1]
        self.player_field = fields[0]
        self.damaged_cells = [[" " for j in range(10)] for i in range(10)]

    def shoot_at(self, coord):
        """
        (tuple) -> (None)
        Reloads the field after opponents move.
        """
        valid_crd = (convert_ltr_coord(coord[0]), coord[1]-1)
        self.ships[valid_crd[0]][valid_crd[1]].shoot_at(valid_crd)
        self.damaged_cells[valid_crd[0]][valid_crd[1]] = "X"

    def field_without_ships(self):
        """
        (None) -> (str)
        Returns a field of current player.
        """
        return field_to_str(self.damaged_cells)

    def field_with_ships(self):
        """
        (None) -> (str)
        This method returns a field of current player with ships in string.
        """
        player_field = [["X" if self.damaged_cells[i][j] == "X" else self.player_field[i][j] for j in range(10)] for i in range(10)]
        return field_to_str(player_field)