import random

zombies = 1
bridges_count = 10
position = [4]
zombies_out = 0
time = 0
bridges = []

def print_bridge(count):
  for i in range(count):
    print(i, sep='', end=' ', flush=True)

def zombie_position(bridges):
  for bridge_position in range(len(bridges)):
    if bridges[bridge_position][0] == "zombie":
      if bridges[bridge_position][1] > 0:
        print('<', end=' ')
      else:
        print('>', end=' ')
    else:
      print(' ', end=' ')
    

for i in range(bridges_count):
  if i in position:
    bridges.append(["zombie", (-1)**((random.randrange(2)))])
  else:
    bridges.append([0, 0])
while zombies:
  time+=1
  print_bridge(bridges_count)
  print(' (time = {} sec)'.format(time))
  for current_position in range(len(bridges)):
    if bridges[current_position][0] == "zombie":
      if bridges[current_position][1] > 0:
        print('<', end=' ')
      else:
        print('>', end=' ')
      next_position = current_position - bridges[current_position][1]
      if current_position - bridges[current_position][1] == 0 or current_position - bridges[current_position][1] == len(bridges) - 1:
        bridges[current_position] = [0,0]
        zombies -= 1
      elif bridges[next_position][0] == "zombie":
        bridges[current_position][1] *= -1
      else:
        bridges[next_position] = bridges[current_position]
        bridges[current_position] = [0,0] 
    else:
      print(' ', end=' ')
  print('')
  # zombies = 0