
"""
In this version 1.0.1, we work on how to improve our computer player's movement, by making him
attack and deffence at the same time, for example if the player make two in row our computer player
need to defence by make an O on the third case, and from this movement our player can now make some defences
by making .
"""
import random,os
def initializeBoard() :
    return [' ' for _ in range(9)]

def emptyCase(index) :
    if board[index] != ' ' :
        return ' '
    else :
        return str(index+1)
def printBoard() :
    global board,X_score,O_score,difficulty
    message = ["**********" if difficulty == -1 else "easy", "medium", "hard"]
    width = len("     Game Difficulty     ")
    padding = [(width - len(message[0])) // 2,(width - len(message[1])) // 2, (width - len(message[2])) // 2]
    difficulty_message = []
    for i in range (3) :
        difficulty_message.append(f"|{' ' * padding[i]}{message[i]}{' ' * padding[i]}|")
    print("    {} | {} | {}   |   {} | {} | {}        ⬤---------------------⬤      ⬤------------------------⬤".format(board[0],board[1],board[2],emptyCase(0),emptyCase(1),emptyCase(2)))
    print("   ---⬤---⬤---  |  ---⬤---⬤---       |     Score Board     |      |     Game Difficulty    |")
    print("    {} | {} | {}   |   {} | {} | {}        ⬤---------------------⬤      ⬤------------------------⬤".format(board[3],board[4],board[5],emptyCase(3),emptyCase(4),emptyCase(5)))
    print("   ---⬤---⬤---  |  ---⬤---⬤---       |   X : {}  |  O : {}   |      {}".format(X_score,O_score, difficulty_message[0] if difficulty==-1 else difficulty_message[difficulty]))
    print("    {} | {} | {}   |   {} | {} | {}        ⬤---------------------⬤      ⬤------------------------⬤".format(board[6],board[7],board[8],emptyCase(6),emptyCase(7),emptyCase(8)))

def boardIsFull() :
    global board
    return board.count(' ')==0

def caseIsempty(pos) :
    return board[pos] == ' '

def thereIsXinRow(i) :
    global board
    x = i // 3
    y = i % 3
    lineH = [board[c] for c in [x * 3, x * 3 + 1, x * 3 + 2]]
    lineV = [board[c] for c in [y, y + 3, y + 6]]
    listeHV = [board[x] for c in [[0, 4, 8], [2, 4, 6]] for x in c if c == i]
    if 'X' in lineH or 'X' in lineV or 'X' in listeHV :
        return True
    return False 
    
def secondMove() :
    global board
    empty_cases = [i for i in range(9) if board[i]==' ']
    if (([0,6,2,8] or empty_cases) and (board[0]=='X' or board[2]=='X' or board[6]=='X' or board[8]=='X')) :
        board[4] = 'O'
        return 4
    else :
        return -1

def PlayerMove() : 
    global board
    test = True 
    while test :
        try :
            pos = input("\nEnter a number (1-9) : ")
        except EOFError :
            exit()
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

def compMove():
    global board
    boardCopy = board.copy()
    # See if there is an incomplete line, exp : a line have two O or have a two X .
    boardNotChanged = True
    X_winningCase = -1
    pre_winningCases = []
    if difficulty >= 1 :
        for i in range(3):
            lineH = [i * 3, i * 3 + 1, i * 3 + 2]
            lineV = [i, i + 3, i + 6]
            if boardNotChanged :
                array = [board[c] for c in lineH]
                if array.count(' ') == 1 :
                    for j in range(3):
                        if board[lineH[j]] == ' ' :
                            if array.count('O') == 2 :
                                board[lineH[j]] = 'O'
                                boardNotChanged = False
                            elif array.count('O') == 0 :
                                X_winningCase = lineH[j]
                elif array.count('O') == 1 and array.count(' ') == 2 :
                    for c in lineH:
                        if board[c] == ' ':
                            pre_winningCases.append(c)

                array = [board[c] for c in lineV]
                if array.count(' ') == 1 :
                    for j in range(3):
                        if board[lineV[j]] == ' ' :
                            if array.count('O') == 2 :
                                board[lineV[j]] = 'O'
                                boardNotChanged = False
                            elif array.count('O') == 0 :
                                X_winningCase = lineV[j]
                elif array.count('O') == 1 and array.count(' ') == 2 :
                    for c in lineV :
                        if board[c] == ' ':
                            pre_winningCases.append(c)
        listeHV = [[0, 4, 8], [2, 4, 6]]
        for i in range(2):
            if boardNotChanged :
                array = [board[c] for c in listeHV[i]]
                if array.count(' ') == 1 :
                    for j in range(3):
                        if board[listeHV[i][j]] == ' ' :
                            if array.count('O') == 2 :
                                board[listeHV[i][j]] = 'O'
                                boardNotChanged = False
                            elif array.count('O') == 0 :
                                X_winningCase = listeHV[i][j]
                elif array.count('O') == 1 and array.count(' ') == 2 :
                    for c in listeHV[i]:
                        if board[c] == ' ':
                            pre_winningCases.append(c)
            
    for i in range(9):
        if boardCopy[i] == ' ' and board[i] != boardCopy[i]:
            pos = i
            print("\nThe player O fill the {}th case\n".format(pos + 1))
            break
    if boardNotChanged:
        if X_winningCase != -1 :
            board[X_winningCase] = 'O'
            pos = X_winningCase

        # add a condition (difficulty == 2) #hard
        
        elif difficulty == 2 and len(pre_winningCases)!=0 :
            # second move
            pos = secondMove()
            if (pos == -1) :
                
            
                t=[0]*9
                for c in pre_winningCases :
                    t[c]+=1
                best_case_choice = pre_winningCases[0]
                for i in range(9) :
                    if t[i]!=0 and t[best_case_choice]<t[i] :
                        # choose the i th case if it have X in its lines .
                        best_case_choice = i

                    # If the two cases have the same chance, then we should choose the case that has X in a line
                    # to make it hard for the opponent to develop a new strategy by going to a clean line to start
                    # working in that line .
                    elif (t[i]==t[best_case_choice] and thereIsXinRow(i)) or t[i]==4:
                        best_case_choice = i
                
                board[best_case_choice] = 'O'
                pos = best_case_choice
            
        else :
            # we used random just for the first movement or at a blocking movements
            # when the board is empty .
            notFullCases = [index for index in range(9) if caseIsempty(index)]
            pos = random.choice(notFullCases)
            board[pos] = 'O'

        print("\nThe player O fill the {}th case\n".format(pos + 1))


def winner(player = 'N') :
    for i in range(3) :
        if (board[i*3] == board[i*3+1] == board[i*3+2] != ' ' or board[i] == board[i+3] == board[i+6] != ' ') :
            if player!='N' :
                if board[i*3]==player :
                    return True
                else :
                    return False
            return True 
        
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        if player!='N' :
            if board[4]==player :
                return True
            else :
                return False
        return True
    return False
def main() :
    global board, X_score, O_score,difficulty
    playAgain = True
    X_score = O_score = 0
    while playAgain :
        os.system('cls') # clear the terminal 
        
        board = initializeBoard()
        difficulty = -1
        print("-----------------")
        print("|  Tic Tac Toe  |")
        print("-----------------")
        printBoard()
        print("--------------------{}".format("-----" if X_score != O_score else ""))
        print("|***Let We {}***|".format("Play Again" if X_score != O_score else "Start"))
        print("--------------------{}".format("-----" if X_score != O_score else ""))
        PlayerStart = 0
        try :
            while True :
                try :
                    difficulty = int(input("Please choose the game difficulty (0 :: easy, 1 :: medium, 2 :: hard): "))
                    break
                except ValueError:
                    print("\nError, you shoud write a number!\n")
            try : 
                x = random.randint(1,6)
                print("random number : ", x)
                if x == int(input("Please, give a number within (1,6) : ")) :
                    print("Yes, u'll start first")
                    
                else :
                    print("Ohh, the computer will start first")
                    PlayerStart = 1
            except ValueError :
                print("\nError, you shoud write a number!\n")
        except EOFError :
            exit()
    
        while not(boardIsFull()) :
            if x%2 == 0 : # O is playing
                compMove()
                if winner() :
                    O_score+=1
                    printBoard()
                    print("Sorry, O\'s the winner, For the next time :(")
                    break
            else :
                PlayerMove()
                if winner() :
                    X_score+=1
                    printBoard()
                    print("Congratulation!!, You win!!!!")
                    break
            x+=1
            print()
            printBoard()
        try :
            playAgain = input("\nYou wanna play again!(Y/N) : ").strip().lower() == "y"
        except EOFError :
            exit()


main()