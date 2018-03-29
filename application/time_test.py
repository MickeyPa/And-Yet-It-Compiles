import timeit
import pyximport; pyximport.install()

from application.StateSpaceTree import StateSpaceTree
from application.GameBoard import GameBoard
from _datetime import datetime

def run():
    s=0
    for i in range(0,30):
        st = StateSpaceTree(GameBoard(board_string="y b b p y p w r r e g r r w g"))
        #st = StateSpaceTree(GameBoard(level=3))
        start = datetime.now()
        st.find_goal_state()
        stop = datetime.now()
        s+=((stop - start).total_seconds() )

    print(s)
run()



