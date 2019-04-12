import itertools
from operator import mul
from math import sqrt
from decimal import Decimal

###
# dot product matrix 2
# https://stackoverflow.com/a/45159105
# https://codereview.stackexchange.com/questions/185916/multiplication-of-any-two-matrices-using-lists-and-for-in-loop
###

def dotdot(a,b):
  return [[sum(itertools.starmap(mul, zip(row, col))) % 100000 for col in zip(*b)] for row in a]
  # return [[sum(map(mul, row, col)) % 65535 for col in zip(*b)] for row in a]

def power(F, n):
  n = 0 if n < 0 else n
  res = F
  while n > 0:
    if n & 1:
      res = dotdot(F, res)
    F = dotdot(F, F)
    n = n >> 1
  return res

def calc(n):
  matrix1 = [[4.0, 13.0], [1.0,4.0]]
  temp = power(matrix1, n-1)
  an = temp[0][0] 
  # bn = temp [1][0]
  result = 2 * an - 1
  # result = Decimal((an + bn * sqrt(13)) % 10000 )
  # result %= 100000
  return int(result) % 100000

print("Input")
n = input("")
n = int(n)
print("Output")
print(calc(n))