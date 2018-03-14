import timeit
s=timeit.timeit('import application.StateSpaceTree',number=1)
print(s*1000)