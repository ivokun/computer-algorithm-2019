import numpy as np
marblesCount = 2000000000
max = 2

def power(matrix, n):
  result = matrix
  while n > 0:
    if n & 1:
      result = np.matmul(matrix, result)
    matrix = np.matmul(matrix, matrix)
    n = n >> 1
    print(n)
  return result


def fibo_mx(n):
  x = np.array([[1,1],[1,0]], dtype='ulonglong')
  b = power(x,n-1)
  return b % 65535

print(fibo_mx(marblesCount))