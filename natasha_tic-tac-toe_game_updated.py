#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 



from turtle import clear


board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    intposition =int(position)
    board[intposition] = mark
   



# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard(board):
    temp_board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
    }
    for k in board.keys():
        if board[k] == ' ':
            temp_board[k] = str(k)
        else:
            temp_board[k] = board[k]

        print(temp_board[1] + ' | ' + temp_board[2] + ' | ' + temp_board[3])
        print('---------')
        print(temp_board[4] + ' | ' + temp_board[5] + ' | ' + temp_board[6])
        print('---------')
        print(temp_board[7] + ' | ' + temp_board[8] + ' | ' + temp_board[9])



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    try:
        intposition = int(position) 
    except ValueError:
        return False
    if intposition >= 1 and intposition <= 9:
        if board[intposition] == ' ':
                result = True
        else:
            result = False
    else: 
        result = False
    
    return result
    
    

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    if board[1] == board[2] == board[3] == player:
        result = True
    elif board[4] == board[5] == board[6] == player:
        result = True
    elif board[7] == board[8] == board[9] == player:
        result = True
    elif board[1] == board[4] == board[7] == player:
        result = True
    elif board[2] == board[5] == board[8] == player:
        result = True
    elif board[3] == board[6] == board[9] == player:
        result = True
    elif board[1] == board[5] == board[9] == player:
        result = True
    elif board[7] == board[5] == board[3] == player:
        result =True
    else:
        result = False
    return result


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for point in board.keys():
        if board[point] == ' ':
            return False
            
    return True


#########################################################
## Copy all your code/c in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

def switch_user():
    global currentTurnPlayer 
    if currentTurnPlayer =='X':
        currentTurnPlayer = 'O'
    else:
        currentTurnPlayer =='O'
        currentTurnPlayer = 'X'

def restart_game():
    restart = input("Do you want to play again? Choose Y(yes) or N(no): ")
    if restart == 'Y':
        result = True
    elif restart == 'N':
        result = False
    return result

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
def game():
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn,: ")
        if  validateMove(move):
            markBoard(move,currentTurnPlayer)
            printBoard(board)
            if checkWin(currentTurnPlayer):
                print(f"{currentTurnPlayer} is the winner!")
                break
            if  checkFull():
                print("It's a tie!")
                break
            switch_user()     
        else:
            print("Wrong move!.Please try again.")

game()

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
if restart_game() == True:
    for k in board:
        board[k] = ' '
    game()  
else:
    print("Thank you for playing!")
