import string
import config
import random
class GameBoard:
    # emptyposition is a tuple containing the index values of the empty slot's position on the gameboard.

    # Tables for reference
    # board = [['A','B','C','D','E'],
    #          ['F','G','H','I','J'],
    #          ['K','L','M','N','O']]
    # indices = [[(0,0),(0,1),(0,2),(0,3),(0,4)],
    #            [(1,0),(1,1),(1,2),(1,3),(1,4)],
    #            [(2,0),(2,1),(2,2),(2,3),(2,4)]]

    #Maps position to indices
    # Example: position_map['A']=(0,0)
    position_map={a:b for a,b in zip([s for s in string.ascii_uppercase[0:24]],[(i,j) for i in range(0,3) for j in range(0,5)])}

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

        pieces=iter(board_string.replace(" ","")) #replace blank spaces with nothing and create an iterator

        for i,row in enumerate(self.board):
            for j,pos in enumerate(row):
                self.board[i][j]=next(pieces)


