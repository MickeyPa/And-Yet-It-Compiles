import timeit
from application.StateSpaceTree import StateSpaceTree
from application.GameBoard import GameBoard
from _datetime import datetime

s=0
for i in range(0,10):
    st = StateSpaceTree(GameBoard(level=3))
    start = datetime.now()
    st.find_goal_state()
    stop = datetime.now()
    s+=((stop - start).total_seconds() )

print(s)




