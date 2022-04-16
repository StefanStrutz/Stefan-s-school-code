#This code was written by Stefan Strutz with a skeleton provided
#by the Cisco Web Academy
#The goal of this code is to make a game of tic-tac-toe. No AI expected
#Future note: this code was written before I learned exceptions
import random
def display_board(board):
    print (f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    """)
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
def enter_move(board):
    while True:
        break_switch = False
        move =int(input ("Your move:"))
        #The format you enter is explained when you start up the code
        counter = 0
        for i in range(3):
            for j in range (3):
                counter += 1
                if move==counter:
                    if board [i][j]=="X" or board [i][j]=="O":
                        print ("Try again")
                    else:
                        board [i][j]="O"
                        break_switch = True
        if break_switch:
            break
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_list = []
    for i in range(3):
        for j in range (3):
            if type(board [i][j]) is int:
                free_list.append ((i,j))
    return free_list
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    free_list = make_list_of_free_fields(board)
    if len(free_list)>=5: #if there too many free spaces then we know victory can't could have happened
        return True
    trans = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] #https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    if[sign, sign, sign] in board:
        print (sign, "is victorious, row. ")
        return False
    elif [sign, sign, sign] in trans:
        print (sign, "is victorious, column. ")
        return False
    elif  board [0][0]== sign and  board [1][1]== sign and  board [2] [2]== sign:
        print (sign, "is victorious. ")
        return False
    elif board [0][2]== sign and  board [1][1]== sign and  board [2] [0]== sign:
        print (sign, "is victorious. ")
        return False
    elif len(free_list)==0:
        print ("Cats game.")
        return False
    else:
        return True
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    empty_spaces = make_list_of_free_fields(board)
    move=empty_spaces[random.randrange(len(empty_spaces))]
    board [move[0]][move[1]] = "X" #this works because board is a list and uses pointers
    return
    # The function draws the computer's move and updates the board.


print ("Let's play tic-tac-toe. I'll make the 1st move.")
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
display_board (board)
print("Just enter the number representing the square you want to fill")
no_end = True
while no_end:
    enter_move (board)
    display_board (board)
    no_end=victory_for(board, "O")
    if not no_end:
        break
    draw_move(board)
    display_board (board)
    no_end=victory_for(board, 'X')

