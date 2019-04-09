import numpy as np
marblesCount = 2000000000
max = 2

def fibo_mx(n):
  x = np.matrix([[1,1],[1,0]])
  b = x**n
  return b

print(fibo_mx(marblesCount))


# def pickMarbles(marbles, maxPick):
#   marbles = marbles + 1
#   ways = [0 for x in range(marbles)]
#   ways[0], ways[1], ways[2] = 1,1,2

#   for i in range(3, marbles):
#     j = 1
#     while j<=maxPick and j<=i:
#       ways[i] += ways[i-j]
#       j = j + 1
#   return ways[marbles-1]

# way = pickMarbles(marblesCount, max) 

# print(way)