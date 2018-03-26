import cProfile
import pstats
from application.time_test import run
#cProfile.run('run()','profile_stats')
p = pstats.Stats('profile_stats')
p.sort_stats('cumtime')
p.print_stats()

