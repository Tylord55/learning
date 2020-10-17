board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player1 = "X"
player2 = "O"


def reset_board():
    global board
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# Prints the current board.
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "\n" +
          board[3] + "|" + board[4] + "|" + board[5] + "\n" +
          board[6] + "|" + board[7] + "|" + board[8])


# Sets the space to X or O.
def set_position(position, player):
    if player == "X":
        board[position] = "X"
    else:
        board[position] = "O"


# Checks to see if the position is free, returns 0 if available.
def position_isvalid(position):
    if board[position] == "-":
        return 0
    else:
        return 1


def turn(player):
    position = str(input("Player " + player + ", enter your move:"))
    # Checks to see if position is 1 through 9 and if the position is free
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or position_isvalid(int(position) - 1) == 1:
        print("Move failed!")
        position = str(input("Player " + player + ", enter your move:"))
    position = int(position) - 1
    set_position(position, player)
    display_board()


def start_game():
    display_board()
    current_turn = 1
    turns = 0
    # Run for 9 turns unless a winner is found before the board is filled.
    while turns < 9:
        if current_turn == 1:
            turn(player1)
            current_turn = 2
        else:
            turn(player2)
            current_turn = 1
        turns += 1
        if check_winner():
            if current_turn == 2:
                print("Player {} has won!".format(player1))
            else:
                print("Player {} has won!".format(player2))
            break
        #print("Turn:", turns)
        if turns == 9:
            print("Game ended in a tie.")
    play_again = input("Press Y to play again:")
    if play_again == "Y" or play_again == "y":
        reset_board()
        start_game()


# Checks all possible winning scenarios.
def check_winner():
    if board[0] == board[1] and board[0] == board[2] and board[0] != "-":
        return True
    elif board[3] == board[4] and board[3] == board[5] and board[3] != "-":
        return True
    elif board[6] == board[7] and board[6] == board[8] and board[6] != "-":
        return True
    elif board[0] == board[3] and board[0] == board[6] and board[0] != "-":
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != "-":
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != "-":
        return True
    elif board[0] == board[4] and board[0] == board[8] and board[0] != "-":
        return True
    elif board[2] == board[4] and board[2] == board[6] and board[2] != "-":
        return True
    else:
        return False


start_game()
