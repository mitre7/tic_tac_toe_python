import random
import os

def clear():
    os.system( 'clear' )

def display_board(board):
    clear()
    
    print("     |     |     ")
    print("  " + board[6] + "  |  " + board[7] + "  |  " + board[8])
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("     |     |     ")
    print("-----------------")
    print("     |     |               7|8|9")
    print("  " + board[0] + "  |  " + board[1] + "  |  " + board[2] + "            4|5|6")
    print("     |     |               1|2|3")

def select_symbol(n1, n2):
    
    user_symbol = input(n1 + " please select your symbol (X or O)\n")
    
    while user_symbol.upper() != 'X' and user_symbol.upper() != 'O':
        user_symbol = input("Invalid symbol. Type again X or O \n")
    
    if user_symbol.upper() == 'X':
        print(n1 + ": X \n" + n2 + ": O")
        return ('X','O')
    else:
        print(n1 + ": O \n" + n2 + ": X")
        return ('O','X')

def has_board_empty_place(board):
    return ' ' in board

def place_marker(board,marker):
    if has_board_empty_place(board):
        position = input("Where do you want to place your marker?\n")
        while position not in '1 2 3 4 5 6 7 8 9'.split() or board[int(position) - 1] != ' ':
            position = input("Invalid number. Please type again\n")
        
        board[int(position) - 1] = marker   

def is_game_over(board,marker):
    if (board[0] == board[4] == board[8] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[4] == board[6] == marker) or (board[3] == board[4] == board[5] == marker) or (board[0] == board[1] == board[2] == marker) or (board[0] == board[3] == board[6] == marker) or (board[2] == board[5] == board[8] == marker) or (board[6] == board[7] == board[8] == marker):
        return True
    else:
        return False

def is_the_board_full(board):
    return ' ' not in board


#Game Starts!!!

print("Welcome to Tic Tac Toe\n")
name1 = input("Player 1 please type your name\n")
name2 = input("Player 2 please type your name\n")
    
ran_number = random.randint(1,2)
    
if ran_number == 1:
    print(name1 + " plays first!")
    symbol = select_symbol(name1, name2)
    name = (name1,name2)
else:
    print(name2 + " plays first!")
    symbol = select_symbol(name2, name1)
    name = (name2,name1)
    
index = 0

board = [' ']
board = board * 9

while True:
    display_board(board)
    print('\n' + name[index] + ": ")
    place_marker(board,symbol[index])
    
    if is_game_over(board,symbol[index]):
        display_board(board)
        print(name[index] + " WINS!!!")
        break
    elif is_the_board_full(board):
        display_board(board)
        print("Tie!")
        break
    else:
        if index == 0: index = 1
        else: index = 0


print("End of the game!!!")
       
