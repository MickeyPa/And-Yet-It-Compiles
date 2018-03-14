import copy
import random


class StateSpaceTree():
    def __init__(self, gameboard):
        self.start_node=Node(copy.deepcopy(gameboard))

    def find_goal_state(self):
        explored_states=[]
        #use dict so we can lookup with O(1)
        explored_gameboards={}
        open_list=[]

        current_node=self.start_node
        while(not current_node.gameboard.check_goal_state()):
            #Expand node if children=empty
            if current_node.children==[]:
                moves=current_node.gameboard.successors()

                #if no more moves go to next node in the open list

                for move in moves:
                    next_gameboard=copy.deepcopy(current_node.gameboard)
                    next_gameboard.move(move)
                    if not str(next_gameboard.board) in explored_gameboards:
                         current_node.add_child(Node(next_gameboard,move=current_node.past_moves+[move]))


            #Go to next node based on the heuristic

            # if no more moves go to next node in the open list
            if current_node.children==[]:
                current_node=open_list[0]
                open_list.pop(0)
            else:
                rand=random.randint(0, len(current_node.children) - 1)
                open_list = open_list + [n for i,n in enumerate(current_node.children) if i != rand]
                current_node=current_node.children[rand]
                explored_states.append(current_node.past_moves[len(current_node.past_moves)-1])
                explored_gameboards[str(current_node.gameboard.board)]=1
        return current_node.past_moves



class Node():
    def __init__(self,gameboard,children=None,move=None):
        # had to do it this way because python==wierd
        if children is None:
            self.children=[]
        else:
            self.children=children

        self.gameboard=gameboard
        self.h=0
        if move is None:
            self.past_moves=[]
        else:
            self.past_moves=move

    def add_child(self,child):
        self.children.append(child)

    # def build_tree(self):
    #
    #     children=self.gameboard.successors()

from application.GameBoard import GameBoard

string = "b r b w w r r b b b b r e r r"
game_board = GameBoard(string)
s=StateSpaceTree(game_board)
print(str(s.find_goal_state()))