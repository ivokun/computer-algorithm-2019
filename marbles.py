marblesCount = 2000000000
max = 2

def multiply(F, M):
  x =  F[0][0] * M[0][0] + F[0][1] * M[1][0]
  y =  F[0][0] * M[0][1] + F[0][1] * M[1][1]
  z =  F[1][0] * M[0][0] + F[1][1] * M[1][0]
  w =  F[1][0] * M[0][1] + F[1][1] * M[1][1]
  F[0][0] = x
  F[0][1] = y
  F[1][0] = z
  F[1][1] = w

def power(F, n):
  if n == 0 or n == 1:
    return
  M = [[1,1],[1,0]]
  power(F, n / 2)
  multiply(F, F)
  if n % 2 != 0:
    multiply(F, M)

def fibo_matrix(n):
  F = [[1,1],[1,0]]
  if n == 0:
    return 0
  power(F, n - 1)
  return F[0][0]

print(fibo_matrix(marblesCount))


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