#The main function 
def main():
    intro()
    board = create_grid()
    print_board(board)
    symbol_1, symbol_2 = ask_symb()



#This function introduces the rules of the game Tic Tac Toe
def intro():
    print("Hello! Welcome to Ceydas Tic Tac Toe game!\n")
    print("Rules: Player 1 and player 2, represented by X and O, take turns"
          " marking the spaces in a 3x3 grid. The player who succeeds in placing"
          " three of their marks in a horizontal, vertical, or diagonal row wins.\n")
    input("Press enter to continue.\n")


#This function creates a blank board
def create_grid():
    print("Here is the playboard:")
    board = [[" ", " ", " "] for _ in range(3)]
    return board


#ask player which symbol, he /she wants to be
def ask_symb():
    symbol_1 = input("Player 1, do you want to be X or O? ")
    symbol_2 = "O" if symbol_1 == "X" else "X"
    print(f"Player 2, you are {symbol_2}.")
    input("Press enter to continue." + "\n")
    return symbol_1, symbol_2


#begins the game
def start_gaming(board, symbol_1, symbol_2):
    player = symbol_1
    count = 0
    while count < 9:
        print("Player " + player + ", it is your turn.")
        row, column = get_input()
        while not is_valid_selection(board, row, column):
            print("Out of boarder or square already filled. Pick another one.")
            row, column = get_input()
        board[row][column] = player
        print_board(board)
        if is_winner(board, player):
            print(f"Player {player}, you won!")
            return
        count += 1
        player = symbol_2 if player == symbol_1 else symbol_1

    print("The board is full. Game over. It's a tie.")

#This function ask for inputs row and column
def get_input():
    row = int(input("Pick a row [0, 1, 2]: "))
    column = int(input("Pick a column [0, 1, 2]: "))
    return row, column


#This function proofs is valid selection
def is_valid_selection(board, row, column):
    if row < 0 or row > 2 or column < 0 or column > 2:
        return False
    return board[row][column] == " "
    

# This function prints the board nice!   
def print_board(board):
    print("---+---+---")
    for r in range(3):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")


# This function checks if any winner is winning
def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
        return True
    return False
    

# Call Main
main()
