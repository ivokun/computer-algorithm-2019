marblesCount = 2000000000
max = 2

# def multiply():

def pickMarbles(marbles, maxPick):
  marbles = marbles + 1
  ways = [0 for x in range(marbles)]
  ways[0], ways[1], ways[2] = 1,1,2

  for i in range(3, marbles):
    j = 1
    while j<=maxPick and j<=i:
      ways[i] += ways[i-j]
      j = j + 1
  return ways[marbles-1]

way = pickMarbles(marblesCount, max) 

print(way)