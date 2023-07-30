#The main function 
def main():
    intro()
    board = create_grid()
    print_board(board)
    symbol_1, symbol_2 = sym()
    is_full(board, symbol_1, symbol_2)


#This function introduces the rules of the game Tic Tac Toe
def intro():
    print("Hello! Welcome to Ceydas Tic Tac Toe game!" + "\n")
    print("Rules: Player 1 and player 2, represented by C and 0, take turns"
    "marking the soaces in a 3*3 grid. The player who succeeds in placing"
    "three of their marks in a horizontal, vertical, or diagonal row wins." + "\n")
    input("Press enter to continue." + "\n")


#This function creates a blank board
def create_grid():
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board



def sym():
    symbol_1 = input("Player 1, do you want to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O. ")
    else:
        symbol_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue." + "\n")
    return symbol_1, symbol_2



def start_gaming(board, symbol_1, symbol_2, count):
    player = 0
    # Decides the turn
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player "+ player + ", it is your turn. ")
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))
    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                           "[left column: enter 0, middle column: enter 1, right column enter 2]"))
        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Pick a row[upper row:"
                        "[enter 0, middle row: enter 1, bottom row: enter 2]:"))
        column = int(input("Pick a column:"
                            "[left column: enter 0, middle column: enter 1, right column enter 2]"))    
    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1       
    else:
        board[row][column] = symbol_2    
    return board


def is_full(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check if the board is full
    while count < 10 and winner:
        start_gaming(board, symbol_1, symbol_2, count)
        print_board(board)
        if count == 9:
            print("The board is full. Game over.")
            if winner:
                print("There is a tie. ")
        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if not winner:
        print("Game over.")    


# This function tells the players that their selection is out of range
def out_of_board():
    print("Out of boarder. Pick another one. ")
    

# This function prints the board nice!   
def print_board(board):
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


# This function checks if any winner is winning
def is_winner(board, symbol_1, symbol_2):
    winner = True
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")  
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")         
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")
    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")
    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")
    return winner
    

def illegal():
    print("The square you picked is already filled. Pick another one.")


# Call Main
main()
