matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

easyMatrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print(easyMatrix[(0,3)])
#problem if we want something in  a 0 slot we'll get an error! fix? the get method!
print(easyMatrix.get((1,4), 0))


