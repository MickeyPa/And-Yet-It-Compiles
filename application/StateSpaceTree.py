import copy
import random
import string

class StateSpaceTree():
    def __init__(self, gameboard):
        self.start_node=Node(copy.deepcopy(gameboard))

    def find_goal_state(self):

        #keep a list of explored gameboards to avoid cycles. Used a dict for O(1) lookup time
        explored_gameboards={}
        open_list=[]
        current_node=self.start_node
        while(not current_node.gameboard.check_goal_state()):

            '''Step 1: Expand current node to calculate all the next states'''
            if current_node.children==[]:
                moves=current_node.gameboard.successors()
                for move in moves:
                    next_gameboard=copy.deepcopy(current_node.gameboard)
                    next_gameboard.move(move)
                    #Ignore states that have already been traversed
                    if not str(next_gameboard.board) in explored_gameboards:
                         n=Node(next_gameboard,move=current_node.past_moves+[move],h=self.evaluate_node_heuristic(next_gameboard))
                         current_node.add_child(n)

            '''Step 2: Evaluate Heuristic and choose the next node'''

            #if the tree reaches the end, take the next node from the open list
            # If no goal state is reached by 20 moves, take the next node from the open list
            if current_node.children==[] or len(current_node.past_moves)>=20:
                current_node=open_list[0]
                open_list.pop(0)

            else:
                hs_of_x=[node.h for node in current_node.children]
                hs_i=hs_of_x.index(min(hs_of_x))
                open_list = open_list + [n for i,n in enumerate(current_node.children) if i != hs_i]
                current_node=current_node.children[hs_i]
                explored_gameboards[str(current_node.gameboard.board)]=1
        return current_node.past_moves

    def evaluate_node_heuristic(self,game_board):
        h = 0
        row_1 = game_board.board[0]
        row_2 = game_board.board[2]
        for i, piece1 in enumerate(row_1):
            distance = 4
            for j, piece2 in enumerate(row_2):
                if piece1 == piece2:
                    if (abs(i-j)) < distance:
                        distance = abs(i-j)
            h += distance
        return h

class Node():
    def __init__(self,gameboard,children=None,move=None,h=float('inf')):
        # had to do it this way because python==wierd
        if children is None:
            self.children=[]
        else:
            self.children=children

        self.gameboard=gameboard
        self.h=h
        if move is None:
            self.past_moves=[]
        else:
            self.past_moves=move

    def add_child(self,child):
        self.children.append(child)

position_map_reverse = {a: b for a, b in
                zip([(i, j) for i in range(0, 3) for j in range(0, 5)], [s for s in string.ascii_uppercase[0:24]])}
# Example: position_map[(0,0)]=A

#creat list of valid inputs for player
def presentPlayerMoves(self):
    playerMoves = []
    for E in self:
        playerMoves.append(position_map_reverse[E])
    return playerMoves


from application.GameBoard import GameBoard

string = "b r b w w r r b b b b r e r r"
game_board = GameBoard(string)
s=StateSpaceTree(game_board)

solution = str(presentPlayerMoves(s.find_goal_state()))

# write solution to output file
with open("output.txt", "a") as f:
    f.write(solution)

#print solution to console
print(solution)
