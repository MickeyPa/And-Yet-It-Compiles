import copy
import random


class StateSpaceTree():
    def __init__(self, gameboard):
        self.start_node=Node(copy.deepcopy(gameboard))

    def find_goal_state(self):
        explored_states=[]
        #use dict so we can lookup with O(1)
        explored_gameboards={}

        current_node=self.start_node
        while(not current_node.gameboard.check_goal_state()):
            #Expand node if children=empty
            if current_node.children==[]:
                moves=current_node.gameboard.successors()
                for move in moves:
                    next_gameboard=copy.deepcopy(current_node.gameboard)
                    next_gameboard.move(move)
                    if not str(next_gameboard.board) in explored_gameboards:
                        current_node.add_child(Node(next_gameboard,move=move))
            #Go to next node based on the heuristic
            current_node=current_node.children[random.randint(0,len(current_node.children)-1)]
            explored_states.append(current_node.move)
            explored_gameboards[str(current_node.gameboard.board)]=1
        return explored_states



class Node():
    def __init__(self,gameboard,children=None,move=None):
        # had to do it this way because python==wierd
        if children is None:
            self.children=[]
        else:
            self.children=children

        self.gameboard=gameboard
        self.h=0
        self.move=move

    def add_child(self,child):
        self.children.append(child)

    # def build_tree(self):
    #
    #     children=self.gameboard.successors()

from application.GameBoard import GameBoard

string = "r e b w r b b b r r r b r b w"
game_board = GameBoard(string)
s=StateSpaceTree(game_board)
print(str(s.find_goal_state()))