import time, random
def fillSpaces(string) :
    listOfSpaces = []
    i, j =0, len(string) - 1
    while i<j :
        if not string[i+2].isalpha() and string[i] == ' ' :
            listOfSpaces.append(i)
            string = string[:i] + '|' + string[i+1:]
        i+=1
        if not string[j-2].isalpha() and string[j] == ' ' :
            listOfSpaces.append(j)
            string = string[:j] + '|' + string[j+1:]
        j-=1
    return listOfSpaces

# boards : contain all the used board in the game, as a matrix .
boards = []
def fillingBoardWithWord(x, y, word, boardTypeIndex) :
    # call the board[boardTypeIndex] to get the board
    # then, fill the specific case
    # in any changes, call a print function with boardTypeIndex as a argument
    pass

# fill a random case by calling then the fillingBoardWithWord 
def animatedFillingBoard(listOfSpaces) :
    while listOfSpaces != [] :
        randomIndex = random.choice(listOfSpaces)
        
        listOfSpaces.remove(randomIndex)

# make a matrix with all the free spaces, and then call the animatedFillingBoard to make it general
# to all the board cases, not just for a case in a ligne .
fillSpaces("|||  | ||| |||  Tic Tac Toe  || || || |  ||")

"""
print("\033c", end='')
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||  | ||| |||  Tic Tac Toe  || || || |  ||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        ||||| ||        || ||| |         ||| |  |||")
print("        ||             ||     ||  |    |      |||||")
print("        ||               Welcome                 ||")
print("        ||||||||||                       ||||||||||")
print("        |||||||||                          ||||||||")
print("        ||||||||||||||               ||||||||||||||")
print("        ||                                       ||")
print("        |||                                     |||")
print("        |||||||  ||                        |  |||||")
print("        |||  ||||||| |  |   ||  |||     ||||   ||||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
time.sleep(0.7)
print("\033c", end='')
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||  | ||| |||  Tic Tac Toe  || || || |  ||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        ||||| ||        || ||| |         ||| |  |||")
print("        ||             ||     ||  |    |      |||||")
print("        ||               Welcome                 ||")
print("        ||||||||||    To Our New Game    ||||||||||")
print("        |||||||||                          ||||||||")
print("        ||||||||||||||               ||||||||||||||")
print("        ||                                       ||")
print("        |||                                     |||")
print("        |||||||  ||                        |  |||||")
print("        |||  ||||||| |  |   ||  |||     ||||   ||||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
time.sleep(0.7)
print("\033c", end='')
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||  | ||| |||  Tic Tac Toe  || || || |  ||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        ||||| ||        || ||| |         ||| |  |||")
print("        ||             ||     ||  |    |      |||||")
print("        ||               Welcome                 ||")
print("        ||||||||||    To Our New Game    ||||||||||")
print("        |||||||||                          ||||||||")
print("        ||||||||||||||  TIC TAC TOE  ||||||||||||||")
print("        ||                                       ||")
print("        |||                                     |||")
print("        |||||||  ||                        |  |||||")
print("        |||  ||||||| |  |   ||  |||     ||||   ||||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
time.sleep(0.7)
print("\033c", end='')
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||  | ||| |||  Tic Tac Toe  || || || |  ||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        ||||| ||        || ||| |         ||| |  |||")
print("        ||             ||     ||  |    |      |||||")
print("        ||               Welcome                 ||")
print("        ||||||||||    To Our New Game    ||||||||||")
print("        |||||||||                          ||||||||")
print("        ||||||||||||||  TIC TAC TOE  ||||||||||||||")
print("        ||                                       ||")
print("        |||     Few Minutes And We'll Start     |||")
print("        |||||||  ||                        |  |||||")
print("        |||  ||||||| |  |   ||  |||     ||||   ||||")
print("        |||||||||||||||||||||||||||||||||||||||||||")

for i in range(5) :
    print(i+1)
    time.sleep(1.0)
print("\033c", end='')
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||  | ||| |||  Tic Tac Toe  || || || |  ||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        ||||| ||        || ||| |         ||| |  |||")
print("        ||                                    |||||")
print("        ||               Please                  ||")
print("        |||            Choose The Game           ||")
print("        |||||||||          Difficulty         |||||")
print("        |||||||     PRESS-KEY            ||||||||||")
print("        ||          :: 0 :: easy  ::             ||")
print("        |||          :: 1 :: medium  ::         |||")
print("        |||||||  ||   :: 2 :: hard  ::     |  |||||")
print("        |||||  |  ||                   |||    |||||")
print("        |||  ||||||  |  |   ||  |||     | ||   ||||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||||||| ")
difficulty = int(input("        ||||||||||| KEY :: "))



# board printing
print("\033c", end='')
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        |||  | ||| |||  Tic Tac Toe  || || || |  ||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
print("        ||||| ||        || ||| |         ||| |  |||")
print("        ||                                    |||||")
print("        ||     X | X | X    |     X | X | X      ||")
print("        |||   ---⬤---⬤---   |    ---⬤---⬤---     ||")
print("        ||||   X | X | X    |     X | X | X     |||")
print("        ||    ---⬤---⬤---   |    ---⬤---⬤---     ||")
print("        |||    X | X | X    |     X | X | X     |||")
print("        ||                                       ||")
print("        |||||||  |||  ||| ||||  |  |||  |||  ||||||")
print("        |||  ||||||| |||  || |||||  ||| ||||   ||||")
print("        |||||||||||||||||||||||||||||||||||||||||||")
"""