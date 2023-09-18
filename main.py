import random
def initializeBoard() :
    return [' ' for _ in range(9)]
def printBoard() :
    print("{} | {} | {} ".format(board[0],board[1],board[2]))
    print("----------")
    print("{} | {} | {} ".format(board[3],board[4],board[5]))
    print("----------")
    print("{} | {} | {} ".format(board[6],board[7],board[8]))
def boardIsFull() :
    return board.count(' ')==0
def caseIsempty(pos) :
    return board[pos-1] == ' '
def PlayerMove() :
    test = True 
    while test :
        pos = input("Enter a number (1-9) : ")
        try :
            pos = int(pos)
            if 0 > pos <= 9 :
                if caseIsempty(pos) :
                    board[pos-1] = 'X'
                    test = False
                else :
                    print("Error, this case is not empty, try an other number!")
            else :
                print("Error, Give a number within the range!")
        except :
            print("Error, you shoud write a number!")
def compMove() :
    notFullCases = [index for index in range(9) if caseIsempty(index)]
    pos = random.choice(notFullCases)
    board[pos] = 'O'

def winner() :
    for i in range(3) :
        if (board[i*3] == board[i*3+1] == board[i*3+2] != ' ' or board[i] == board[i+3] == board[i+6] != ' ') :
            return True
        
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False
def main() :
    global board
    board = initializeBoard()
    printBoard()
    x = 0
    while not(boardIsFull()) :
        if x%2 == 0 : # O is playing
            compMove()
            if winner() :
                print("Sorry, O/'s the winner, For the next time :(")
                break
        else :
            PlayerMove()
            if winner() :
                print("Congratulation!!, You win!!!!")
                break
        x+=1
        printBoard()

main()