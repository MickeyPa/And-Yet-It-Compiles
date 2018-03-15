import timeit

# create new file
f = open("output.txt", "a")

f.write("\n\nGameboard #1:\n")

# run the operation
s = timeit.timeit('import application.StateSpaceTree', number=1)
print(s*1000)

# print time information to the file
f.write("\nTime: " + str(s*1000) + " ms.\n")

# TODO print total number of moves it took to solve ALL the puzzles

f.close()
