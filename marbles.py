# import numpy as np
import itertools
marblesCount = 2000000000
max = 2

def dot1d(a,b):
  return sum(x*y for x,y in zip(a,b))

def dot2d(a,b):
  product = [dot1d(x,y) for x,y in itertools.product(a,b)]
  return [product[i::len(a)] for i in range(len(a))]

def power(F, n):
  res = F
  while n > 0:
    if n & 1:
      # res = np.dot(F, res)
      # res = multiply_matrix(F, res)
      res = dot2d(F, res)
    # F = np.dot(F, F)
    # F = multiply_matrix(F, F)
    F = dot2d(F, F)
    n = n >> 1
  return res


def fibo_mx(n, step=2):
  if step < 2:
    return
  # x = np.eye(step,step, k=-1, dtype=object)
  # x[0] = np.ones(step)
  x = []
  for row in range(step):
    inner_x = []
    for col in range(step):
      if row == 0:
        inner_x.append(1)
      elif row - 1 == col:
        inner_x.append(1)
      else:
        inner_x.append(0)
    x.append(inner_x)
  b = power(x,n-1)
  return b [0][1] if step == 2 else b[0][0]

print(fibo_mx(2000))