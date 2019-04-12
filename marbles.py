import itertools
from operator import mul
###
# dot product matrix
# https://stackoverflow.com/a/35244370
###

def dot1d(a,b):
  return sum(x*y for x,y in zip(a,b))

def dot2d(a,b):
  product = [dot1d(x,y) % 65535 for x,y in itertools.product(a,b)]
  return [product[i::len(a)] for i in range(len(a))]

###
# dot product matrix 2
# https://stackoverflow.com/a/45159105
# https://codereview.stackexchange.com/questions/185916/multiplication-of-any-two-matrices-using-lists-and-for-in-loop
###

def dotdot(a,b):
  return [[sum(itertools.starmap(mul, zip(row, col))) % 65535 for col in zip(*b)] for row in a]
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

def make_matrix(step):
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
  return x

def fibo_mx(n, step=2):
  x = make_matrix(step)
  b = power(x,n-1)
  return b[0][1] if step == 2 else b[0][0]

print("Input")
marblesCount = input("")
maxPick = input("")
marblesCount = int(marblesCount)
maxPick = 2 if maxPick == '' else int(maxPick)
print("Output")
print(fibo_mx(marblesCount,maxPick))