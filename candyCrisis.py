###########################################################################
# MAIN DRIVER
###########################################################################

import ast  # used to convert str to tuple
from application.GameBoard import GameBoard

print()
print("HELLO AND WELCOME TO CANDY CRISIS, THE MOST DELICIOUS GAME IN TOWN!")
# print("Please specify the path to your gameboard configuration:")
# gbFilePath = input()

# Ask if import or level choice is desired?

# Import file
file = open("Sample_Data.txt", 'r', encoding="utf8")
gameStrings = []

# Check if game is solvable. If it is, add it to gameStrings
for string in file.read().split("\n"):
    game = string.split(" ")

    # check if game has exactly fifteen pieces
    exactNumPieces = True
    if len(game) != 15:
        exactNumPieces = False

    # check if all pieces are single characters
    allChars = True
    for piece in game:
        if len(piece) > 1:
            allChars = False
            break

    # check if game has ONLY 1 empty position e
    onlyOneE = True
    if game.count('e') != 1:
        onlyOneE = False

    # check if game contains AT LEAST 5 pairs of letters
    pairs = []
    numPairs = 0
    for piece in game:
        if pairs.count(piece) == 1:
            numPairs += 1
            pairs.remove(piece)
        else:
            pairs.append(piece)

    # if both are true, append string to gameStrings, else append a string describing the FIRST error found.
    if (numPairs >= 5) and onlyOneE and exactNumPieces and allChars:
        gameStrings.append(string)
    elif not exactNumPieces:
        gameStrings.append(': Does not contain exactly fifteen pieces.')
    elif not onlyOneE:
        gameStrings.append(': Does not contain exactly one empty position.')
    elif not allChars:
        gameStrings.append(': Not all game pieces are single characters.')
    else:
        gameStrings.append(': Game is not solvable.')

# Close input file
file.detach()

# Start running games
gameNum = 0
for string in gameStrings:
    gameNum += 1

    # Check if game is NOT playable
    if string[:1] == ':':
        print("Game #" + (gameNum+1) + " is not playable " + string)
        continue

    g = GameBoard(string)

    # ASK HERE if want to run automatic mode or not.

    print("Here's game #" + gameNum + "!")
    print("Woohoo! This is your gameboard. Let's get playing!")
    turnNum = 0  # number of turns in the game
    goalState = False
    while not goalState:
        turnNum += 1
        # I did this for the gui
        gui_board=list(map(list,list(zip([p for row in g.board_state_helper for p in row],[p for row in g.board for p in row]))))
        print(gui_board)
        # print(g.board[0])
        # print(g.board[1])
        # print(g.board[2])
        # print()

        valid = False
        # loop until they enter a valid input
        while not valid:
            e=g.get_empty_position()
            s=g.successors()
            print("Your possible moves are:")
            print(s)
            print()
            print("[Turn #", turnNum, "] What is your move?")
            nextMove=ast.literal_eval(input())
            print()

            # search set of successors to see if input is valid
            if nextMove in s:
                    valid = True

            if not valid:
                print("Oopsie Daisy! Thats not a valid move. Let's try this again.")
        # end [while not valid]

        g.move(nextMove)
        print("Nice move!")
        if g.check_goal_state():
            goalState = True
        else:
            print("Here is your new-and-improved gameboard.")

    # end [while not goalState]

    print("CONGRATULATIONS! YOU HAVE WON THE GAME! EUREKA! FELICITATIONS! HAPPY BIRTHDAY!")

# end [for string in gameStrings]

