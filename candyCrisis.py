###########################################################################
# MAIN DRIVER
###########################################################################

import ast  # used to convert str to tuple

print()
print("HELLO AND WELCOME TO CANDY CRISIS, THE MOST DELICIOUS GAME IN TOWN!")
#print("Please specify the path to your gameboard configuration:")
#gbFilePath = input()

# !!!!! CALLS THE IMPORT GAMEBOARD FEATURE and creates gameboard object with it

from application.GameBoard import GameBoard
g=GameBoard()

print("Woohoo! This is your gameboard. Let's get playing!")
turnNum = 0 # number of turns in the game
goalState = False
while not goalState:
    turnNum += 1
    print(g.board[0])
    print(g.board[1])
    print(g.board[2])
    print()

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

