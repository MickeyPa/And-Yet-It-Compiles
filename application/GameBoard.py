import string
import config
import random


class GameBoard:
    # empty_position is a tuple containing the index values of the empty slot's position on the gameboard.

    # Tables for reference
    # board = [['A','B','C','D','E'],
    #          ['F','G','H','I','J'],
    #          ['K','L','M','N','O']]
    # indices = [[(0,0),(0,1),(0,2),(0,3),(0,4)],
    #            [(1,0),(1,1),(1,2),(1,3),(1,4)],
    #            [(2,0),(2,1),(2,2),(2,3),(2,4)]]

    # Maps position to indices
    # Example: position_map['A']=(0,0)

    position_map = {a: b for a, b in
                    zip([s for s in string.ascii_uppercase[0:24]], [(i, j) for i in range(0, 3) for j in range(0, 5)])}

    def __init__(self,board_string=None,level=1):
        #if no string is provided, get random string
        if board_string is None:
            board_string=self.randomize_board_string(level)


        self.__create_board_from_string(board_string)



    def randomize_board_string(self,level):
        pieces=config.levels[level]
        board_string='e'
        for piece, count in pieces.items():
            board_string=board_string+piece*count
        bs_list=list(board_string)
        random.shuffle(bs_list)
        return ''.join(bs_list)



    def __create_board_from_string(self,board_string):

        #Create 3x5 empty board
        self.board = [['e' for i in range(5)] for i in range(3)]
        self.board_state_helper=[list(range(0,5)),list(range(5,10)),list(range(10,15))]
        pieces=iter(board_string.replace(" ","")) #replace blank spaces with nothing and create an iterator

        for i,row in enumerate(self.board):
            for j,pos in enumerate(row):
                self.board[i][j]=next(pieces)



    def get_empty_position(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == 'e':
                    return (i, j)



    # Determine Successors (possible moves) based on current position of e (empty slot).
    def successors(self):

        empty_position = self.get_empty_position()
        successors = []
        if empty_position == (0, 0):  # A
            successors = [(1, 0), (0, 1)]
            # F,B

        elif empty_position == (0, 1):  # B
            successors = [(0, 0), (1, 1), (0, 2)]
            # A,G,C

        elif empty_position == (0, 2):  # C
            successors = [(0, 1), (1, 2), (0, 3)]
            # B,H,D

        elif empty_position == (0, 3):  # D
            successors = [(0, 2), (1, 3), (0, 4)]
            # C,I,E

        elif empty_position == (0, 4):  # E
            successors = [(0, 3), (1, 4)]
            # D,J

        elif empty_position == (1, 0):  # F
            successors = [(0, 0), (2, 0), (1, 1)]
            # A,K,G

        elif empty_position == (1, 1):  # G
            successors = [(0, 1), (1, 0), (1, 2), (2, 1)]
            # F,B,L,H

        elif empty_position == (1, 2):  # H
            successors = [(1, 1), (0, 2), (2, 2), (1, 3)]
            # G,C,M,I

        elif empty_position == (1, 3):  # I
            successors = [(1, 2), (0, 3), (2, 3), (1, 4)]
            # H,D,N,J

        elif empty_position == (1, 4):  # J
            successors = [(1, 3), (0, 4), (2, 4)]
            # I,E,O

        elif empty_position == (2, 0):  # K
            successors = [(1, 0), (2, 1)]
            # F,L

        elif empty_position == (2, 1):  # L
            successors = [(2, 0), (1, 1), (2, 2)]
            # K,G,M

        elif empty_position == (2, 2):  # M
            successors = [(2, 1), (1, 2), (2, 3)]
            # L,H,N

        elif empty_position == (2, 3):  # N
            successors = [(2, 2), (1, 3), (2, 4)]
            # M,I,O

        elif empty_position == (2, 4):  # O
            successors = [(2, 3), (1, 4)]
            # N,J

        return successors



    # Perform the move of the empty slot.
    def move(self, new_position):

        # new_position = position_map[new_position] #if we decide to pass in letter values in stead of tuples.

        # new_position is like empty_position; A tuple containing the index values for its position on the board.
        if new_position not in self.successors():
            # trying to move a piece that is not an immediate successor
            return  # create exception?

        empty_position = self.get_empty_position()
        o=self.board_state_helper[new_position[0]][new_position[1]]
        n=self.board_state_helper[empty_position[0]][empty_position[1]]

        self.board_state_helper[empty_position[0]][empty_position[1]]= o
        self.board_state_helper[new_position[0]][new_position[1]]=n

        self.board[empty_position[0]][empty_position[1]] = self.board[new_position[0]][new_position[1]]
        self.board[new_position[0]][new_position[1]] = 'e'

    # check goal state
    def check_goal_state(self):
        for x in range(0, 5):
            if self.board[0][x] != self.board[2][x]:
                return False

        return True

