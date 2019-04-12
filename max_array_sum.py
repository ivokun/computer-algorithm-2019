def find_sum(array):
  n = len(array)
  max_so_far = array[0]
  max_ending_here = array[0]
  position = 0
  s = 0
  for i in range(1, n):
    max_ending_here += array[i]
    if max_ending_here < array[i]:
      max_ending_here = array[i]
      s = i
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here
      position = (s+1,i+1)
  return position, max_so_far

print("Input")
array = list(map(int, input().split(' ')))
print("Output")
interval, max_sum = find_sum(array)
print("{0}:{1}".format(interval, max_sum))