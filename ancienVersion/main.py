import random
def initializeBoard() :
    return [' ' for _ in range(9)]
def printBoard() :
    print("    {} | {} | {}   |   1 | 2 | 3".format(board[0],board[1],board[2]))
    print("   ---⬤---⬤---  |  ---⬤---⬤---")
    print("    {} | {} | {}   |   4 | 5 | 6".format(board[3],board[4],board[5]))
    print("   ---⬤---⬤---  |  ---⬤---⬤---")
    print("    {} | {} | {}   |   7 | 8 | 9  ".format(board[6],board[7],board[8]))
def boardIsFull() :
    return board.count(' ')==0
def caseIsempty(pos) :
    return board[pos] == ' '
def PlayerMove() :
    test = True 
    while test :
        pos = input("\nEnter a number (1-9) : ")
        try :
            pos = int(pos)
            if 0 < pos <= 9 :
                if caseIsempty(pos-1) :
                    board[pos-1] = 'X'
                    test = False
                else :
                    print("\nError, this case is not empty, try an other number!\n")
            else :
                print("\nError, Give a number within the range!\n")
        except :
            print("\nError, you shoud write a number!\n")
def compMove() :
    notFullCases = [index for index in range(9) if caseIsempty(index)]
    pos = random.choice(notFullCases)
    board[pos] = 'O'
    print("\nThe player O fill the {}th case\n".format(pos+1))

def winner() :
    for i in range(3) :
        if (board[i*3] == board[i*3+1] == board[i*3+2] != ' ' or board[i] == board[i+3] == board[i+6] != ' ') :
            return True
        
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False
def main() :
    global board
    playAgain = True
    while playAgain :
        board = initializeBoard()
        print("-----------------")
        print("|  Tic Tac Toe  |")
        print("-----------------")
        printBoard()
        print("--------------------")
        print("|***Let We Start***|")
        print("--------------------")
        x = 0
    
        while not(boardIsFull()) :
            if x%2 == 0 : # O is playing
                compMove()
                if winner() :
                    printBoard()
                    print("Sorry, O/'s the winner, For the next time :(")
                    break
            else :
                PlayerMove()
                if winner() :
                    printBoard()
                    print("Congratulation!!, You win!!!!")
                    break
            x+=1
            print()
            printBoard()
        playAgain = input("\nYou wanna play again!(Y/N) : ").strip().lower() == "y"


main()