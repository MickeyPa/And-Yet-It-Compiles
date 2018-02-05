import string
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

    def __init__(self,board=None,level=1):
        if board is None:
            self.board=self.randomize_board(level)
        else:
            self.board=board
        self.empty_position==(0,0)

    def randomize_board(self,level):
        pass