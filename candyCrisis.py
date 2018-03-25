###########################################################################
# MAIN DRIVER
###########################################################################
from datetime import datetime
from application.graph_render import render
import ast  # used to convert str to tuple
import string
from application.GameBoard import GameBoard
from application.StateSpaceTree import StateSpaceTree
print()
print("HELLO AND WELCOME TO CANDY CRISIS, THE MOST DELICIOUS GAME IN TOWN!")
# print("Please specify the path to your gameboard configuration:")
# gbFilePath = input()

# Ask if import or level choice is desired?

# Import file
import os
file_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"Sample_Data.txt")
file = open(file_path, 'r', encoding="utf8")
gameStrings = []

# convert character into tuple, ex: A into (0,0)
position_map = {a: b for a, b in
                zip([s for s in string.ascii_uppercase[0:24]], [(i, j) for i in range(0, 3) for j in range(0, 5)])}
# Example: position_map['A']=(0,0)

# convert character into tuple, ex: (0,0) into A
position_map_reverse = {a: b for a, b in
                zip([(i, j) for i in range(0, 3) for j in range(0, 5)], [s for s in string.ascii_uppercase[0:24]])}
# Example: position_map[(0,0)]=A

#creat list of valid inputs for player
def presentPlayerMoves(self):
    playerMoves = []
    for E in self:
        playerMoves.append(position_map_reverse[E])
    return playerMoves

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
        print("Game #" + gameNum + " is not playable " + string)
        continue

    g = GameBoard(string)

    # ASK HERE if want to run automatic mode or not.

    print("Here's game #" + str(gameNum) + "!")
    print("Woohoo! This is your gameboard. Let's get playing!")
    turnNum = 0  # number of turns in the game
    goalState = False
    automatic_mode=False
    automatic_moves=[]
    while not goalState:
        turnNum += 1
        # I did this for the gui
        gui_board=list(map(list,list(zip([p for row in g.board_state_helper for p in row],[p for row in g.board for p in row]))))
        print(gui_board)
        #print(g.board[0])
        #print(g.board[1])
        #print(g.board[2])
        print()

        valid = False
        # loop until they enter a valid input
        while not valid:
            e=g.get_empty_position()
            s=g.successors()
            print("Your possible moves are:")
            nextPossibleMoves = presentPlayerMoves(s)
            print(nextPossibleMoves)
            print()
            print("[Turn #", turnNum, "] What is your move? Type auto to solve the puzzle")
            if automatic_mode:
                nextMove=automatic_moves.pop(0)
                print("automatic move chose: ",position_map_reverse[nextMove])
            else:
                nextMove=input()
                if nextMove=='auto':
                    automatic_mode=True
                    state_space_tree = StateSpaceTree(g)
                    start =datetime.now()

                    automatic_moves=state_space_tree.find_goal_state()

                    stop = datetime .now()
                    render(state_space_tree)
                    with open("output.txt", "a") as f:
                        print("Solution ",end="[")
                        for m in automatic_moves:
                            f.write("%s " % position_map_reverse[m])
                            print(position_map_reverse[m],end=" ")
                        f.write("\n")
                        print("] took "+str(round((stop-start).total_seconds()*1000))+" ms",end="\n")
                        f.write(str(round((stop-start).total_seconds()*1000)))
                        f.write("ms \n")


                    nextMove = automatic_moves.pop(0)
                    print("automatic move chose: ",position_map_reverse[nextMove])
                else:

                    nextMove = position_map[nextMove]
                    print()



            # search set of successors to see if input is valid
            if nextMove in s:
                    valid = True

            if not valid:
                print("Oopsie Daisy! Thats not a valid move. Let's try this again.")
        # end [while not valid]

        g.move(nextMove)
        print("Nice move!")
        print("==================================================================================================================================")
        if g.check_goal_state():
            goalState = True
            gui_board = list(map(list, list(
                zip([p for row in g.board_state_helper for p in row], [p for row in g.board for p in row]))))
            print(gui_board)
        else:
            print("Here is your new-and-improved gameboard.")

    # end [while not goalState]

    print("CONGRATULATIONS! YOU HAVE WON THE GAME! EUREKA! FELICITATIONS! HAPPY BIRTHDAY!")
    print("Press any key to continue")
    input()

# end [for string in gameStrings]
