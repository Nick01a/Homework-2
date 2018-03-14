from game import Game

print("Game Battleship\n")
game = Game()
while True:
    print("Field of first player: ")
    print(game.field_with_ships())
    print("\n Field of second player: ")
    print(game.field_without_ships())
    game.read_position()
