import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-","-","-"]
currentPlayer="X" #initialising this variable with string X
winner=None
gameRunning=True

#printing the gameboard
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take player input
def playerInput(board):
    #ask user to pick a number b/w 1-9 where each number represents a position on the board
    inp=int(input("Enter a number 1-9 to choose a position: "))
    #now to ensure that the input is b/w 1-9 and also not occupied by another user
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        #board[inp-1] ensures that the chosen position is empty like 0 index is 1 position so inp-1
        board[inp-1]=currentPlayer
    else:
        print("Invalid spot/input")


#check for win or tie
def checkHorizontal(board):
    global winner
    #the global variable indicates that any change made to winner variable within the function changes it throughout the whole program
    if board[0]==board[1]==board[2] and board[1]!="-": 
        #checking that whether the horizontal places have an equal value and that value is not a "-"
        winner=board[0] #could say board[1] or 2
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True

def checkVertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
     
def checkDiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True

def checkTie(board):
    global gameRunning
    global winner
    if "-" not in board: 
        #because the board has being filled out yet no win cases have being made
        printBoard(board)
        print("it's a tie")
        gameRunning=False #game stops running here
        winner=None

def checkWin(): #no board in it as no board modified in the function, just functions called
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")
        #cant use a break statement w/o a for or while or any loop in python
#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"

#for computer to make a move
def computer(board):
    while currentPlayer=="O":
        position=random.randint(0,8)#for a position on board
        if board[position]=="-":
            board[position]="O"
            switchPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
