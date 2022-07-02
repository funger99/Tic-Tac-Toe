# There are two players
# I made a Player class
# Each player has the following attributes (attributes are variables inside of a class):

# 1. character (string): 'x' or 'o' each player is either x or o
# 2. turn (boolean): turn can be true or false. If player 1's turn is equal to True, that means it's their turn to play
# 3. p_num (int): this is just the player number, for example, player 2 has a p_num = 2
# 4. row and col (int): these are the positions where each player wants to place their character: 'x' or 'o'

# example: let's say player 1 chose a character of 'x', and wanted to place the x in the center (shown below)

# ['_', '_', '_']
# ['_', 'x', '_']
# ['_', '_', '_']

# then player 1's row = 2 and col = 2

class Player:
    def __init__(self, character, turn, p_num, score):
        self.character = character
        self.turn = turn
        self.p_num = p_num
        self.score = score
        self.row = None
        self.col = None

    # this function assigns values to a player object/instance's row and col attribute
    # this function was called inside the "place_character" function
    def move(self, r, c):
        self.row = r
        self.col = c

# The function below will print out the grid
def generate_grid(player, g1, g2, g3):

    if player.row == 1:
        g1[player.col-1] = player.character
    elif player.row == 2:
        g2[player.col - 1] = player.character
    else:
        g3[player.col - 1] = player.character

    print(g1)
    print(g2)
    print(g3)
    print()

# The function allows Player 1 to either choose x or o as their character
# Player 2 will be automatically assigned the other character that player 1 didn't choose
def choose_character(p1, p2):

    while True:
        p1_character = input("Player 1, choose your character (Type x or o): ")
        print()
        if p1_character != 'o' and p1_character != 'x':
            print("Choose x or o, right the fuck now")
            print()
            continue
        if p1_character == 'x':
            p2_character = 'o'
        else:
            p2_character = 'x'
        break

    p1.character = p1_character
    p2.character = p2_character
    return

# The function below let's the player whose turn it is, to choose where they want to place their character on the grid
def place_character(player, g1, g2, g3):

    print(f"Player {player.p_num} place your character")
    print()

    while True:
        while True:
            player_row = int(input("Row (Type 1 to 3): "))
            print()
            if player_row > 3 or player_row < 1:
                print("I said 1 to 3 nigga... ")
                print()
                continue
            break

        while True:
            player_col = int(input("Column (Type 1 to 3): "))
            print()
            if player_col > 3 or player_col < 1:
                print("I said 1 to 3 nigga... ")
                print()
                continue
            break

        if not valid_move(player_row, player_col, g1, g2, g3):
            print("Invalid move! ")
            print()
            continue
        else:
            break

    # if the move chosen by the player is valid, then we will break out of the while loop
    # and then assign the chosen row and column value to the player's row and col attributes
    player.move(player_row, player_col)

    return

# The function below checks whether the move a player made is valid
# Let's say player 1 places an 'x' in row 2, column 2
# Then player 2 will not be able to place their 'o' in the same place, or the function will return False
def valid_move(r, c, g1, g2, g3):
    if r == 1:
        if g1[c-1] != '_':
            return False
    elif r == 2:
        if g2[c-1] != '_':
            return False
    elif r == 3:
        if g3[c-1] != '_':
            return False

    return True


def check_win(g1, g2, g3):
    if check_rows(g1, g2, g3) != '_':
        return check_rows(g1, g2, g3)

    elif check_col(g1, g2, g3) != '_':
        return check_col(g1, g2, g3)

    elif check_diagonals(g1, g2, g3) != '_':
        return check_diagonals(g1, g2, g3)

    return '_'

def check_rows(g1,g2,g3):
    for r in [g1,g2,g3]:
        if len(set(r)) == 1:
            return r[0]

    return '_'

def check_col(g1,g2,g3):
    for i in range(len(g1)):
        if len({g1[i], g2[i], g3[i]}) == 1:
            return g1[i]

    return '_'

def check_diagonals(g1,g2,g3):
    res = [g1,g2,g3]
    s = set()
    for i in range(len(g1)):
        s.add(res[i][i])

    if len(s) == 1:
        return res[0][0]
    s = set()

    for i in range(len(g1)):
        s.add(res[i][2-i])

    if len(s) == 1:
        return res[0][2]

    return '_'

# The function below is called the "main function"
# Typically, a main function is where you call the other functions in order to perform a task
# Our task is to run the game, play tic tac toe

def main():
    # here we are creating objects from the class "Player"
    # this is also called creating instances of the class "Player"
    # we are creating 2 instances of the class "Player", which are player_1 and player_2
    # player_1 and player_2 will have attributes and methods of the class "Player"
    # e.g. both player 1 and player 2 will have their own character variable (which will either be x or o)
    player_1 = Player(None, True, 1, 0)
    player_2 = Player(None, False, 2, 0)

    while True:
        # printing out the grid at the start of the game
        grid1 = ['_', '_', '_']
        grid2 = ['_', '_', '_']
        grid3 = ['_', '_', '_']
        print(grid1)
        print(grid2)
        print(grid3)
        print()

        # calling the choose character function
        choose_character(player_1, player_2)

        play = True
        count = 0

        while play:

            if player_1.turn:
                place_character(player_1, grid1, grid2, grid3)
                generate_grid(player_1, grid1, grid2, grid3)
            else:
                place_character(player_2, grid1, grid2, grid3)
                generate_grid(player_2, grid1, grid2, grid3)

            count += 1

            if check_win(grid1, grid2, grid3) == player_1.character:
                print("Player 1 wins!")
                player_1.score += 1
                print(f"Player 1 Score: {player_1.score}")
                print(f"Player 2 Score: {player_2.score}")
                play = False
            elif check_win(grid1, grid2, grid3) == player_2.character:
                print("Player 2 wins!")
                player_2.score += 1
                print(f"Player 1 Score: {player_1.score}")
                print(f"Player 2 Score: {player_2.score}")
                play = False
            elif count == 9:
                print("It's a tie!")
                print(f"Player 1 Score: {player_1.score}")
                print(f"Player 2 Score: {player_2.score}")
                play = False


            # once a player has placed their character on the grid, it's the other player's turn
            # so if it was player 1's turn, we have to make it player 2's turn now
            # so if player_1.turn is True, not player_1.turn is False
            player_1.turn = not player_1.turn
            player_2.turn = not player_2.turn

            # in this while loop we will keep alternating between player 1 and player 2's turn until the game is over
            # I haven't coded for the game to be over. You will need to do that.

        play_again = input("Do you want to play again? (Type y or n): ")
        if play_again == 'n':
            break

# remember that we have to call a function in order to use it (run what's written in the function)
main()







