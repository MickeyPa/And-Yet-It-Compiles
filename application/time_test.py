import timeit
import pyximport; pyximport.install()

from application.StateSpaceTree import StateSpaceTree
from application.GameBoard import GameBoard
from _datetime import datetime

def run():
    s=0
    for i in range(0,10):
        st = StateSpaceTree(GameBoard(board_string="g b r w p p y r b g w e r r y"))
        #st = StateSpaceTree(GameBoard(level=4))
        start = datetime.now()
        st.find_goal_state()
        stop = datetime.now()
        s+=((stop - start).total_seconds() )

    print(s)
run()



