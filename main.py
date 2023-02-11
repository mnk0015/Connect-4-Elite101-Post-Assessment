#When a player chooses a column, the token drops down to the lowest, unoccupied space
#- For our game, the board will be 6 x 6
#- Each time a player adds a token to the board, your game should check if they won, and also update the board and reprint it
#- Players tokens can be whatever you want… Xs and Os, 1s and 2s, Rs and Bs, etc.

print("WELCOME TO CONNECT 4!")
user1 = input("Player 1 Name: \n")
user2 = input("Player 2 Name: \n")

board = [['-' for x in range(6)] for y in range(6)]

def print_board():
    for row in board:
        print(' '.join(row))

def drop_circle(column, player):
    for i in range(5, -1, -1):
        if board[i][column] == '-':
            board[i][column] = player
            return

def win_check(player):
    # check horizontal
    for row in range(6):
        for col in range(3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # check vertical
    for row in range(3):
        for col in range(6):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # check positive slope diagonals
    for row in range(3):
        for col in range(3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # check negative slope diagonals
    for row in range(3, 6):
        for col in range(3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

    return False

def game():
    player = 'X'
    while True:
        print_board()
        column = None
        while column is None:
            try:
                user_input = input(f"{user1 if player == 'X' else user2}, choose a column (1-6): ")
                column = int(user_input) - 1
                if not (0 <= column < 6):
                    print("Please enter a number between 1 and 6.")
                    column = None
            except ValueError:
                print("Please enter a number between 1 and 6.")
                column = None
        drop_circle(column, player)
        if win_check(player):
            print_board()
            print(f"{user1 if player == 'X' else user2} has won!")
            break
        if player == 'O':
            player = 'X'
        else:
            player = 'O'
    play_again = input("Want to play again? Enter y or n.")
    if play_again == "y":
      game()
    elif play_again == "n":
      exit()
    else:
      play_again()

game()

print_board()