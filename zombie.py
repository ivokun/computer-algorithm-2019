import random

print("="*50)
print("Walking Dead")
print("="*50)
zombies = int(input("Zombies = "))
bridge_length = int(input("Bridge length = "))
position = input("Put initial position = ").split()
zombies_out = 0
time = 0
bridge = []

for position in range(bridge_length):
  bridge.append(0)

print(bridge)