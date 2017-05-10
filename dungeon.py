import random

# take input for movement
# move player, unless invalid move
# check for win/loss
# clear screen and redraw grid

CELLS = [ (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
          (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
          (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
          (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
        ]


def get_locations():
    '''
    :return: a tuple of tuples indicating random
    locations for the monster, the exit door, and the
    player starting position
    '''
    return random.sample(CELLS, 3)

def move_player(player, move):
    '''
    :param player: a tuple indicating player's current
    location on the map
    :param move: a string indicating the space to which
    the player would like to move
    :return: a tuple indicating the player's new location

    if move == LEFT, x - 1
    if move == RIGHT, x + 1
    if move == UP, y - 1
    if move == DOWN, y + 1
    '''
    x, y = player
    if move == 'LEFT':
        x -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'UP':
        y -= 1
    elif move == 'DOWN':
        y += 1
    else:
        print("That direction is invalid. Please try again")
        pass
    return x, y


def get_moves(player):
    '''
    :param player: a tuple indicating the 2-D location of
    the player on the map
    :return: a list of valid moves based on the player's
    current position

    if player's y value == 0, UP is not a valid move
    if player's y value == 4, DOWN is not a valid move
    if player's x value == 0, LEFT is not a valid move
    if player's x value == 4, RIGHT is not a valid move
    '''
    moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    x, y = player
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    return moves

def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def game_loop():
    monster, exit, player = get_locations()
    playing = True

    while playing == True:
        draw_map(player)
        valid_moves = get_moves(player)

        print('You are currently in room {}'.format(player))
        print("You may move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                print("\n You have fallen to the terror of THE DUNGEON \n * * * GAME OVER * * *")
                playing = False
            if player == exit:
                print("\n CONGRATULATIONS \n You have escaped THE DUNGEON")
                playing = False
        else:
            input("You may not move beyond the limits of THE DUNGEON. Please enter a valid move.")
            continue
    else:
        if input("Would you like to play again? Y/N").upper() != "N":
            game_loop()

print("Welcome to THE DUNGEON")
input("Press RETURN to start the game.")
game_loop()



