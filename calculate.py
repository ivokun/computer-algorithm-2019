p = 1
i = 1
while 1:
  try:
    raw_num = input("Integer = ")
    num = int(raw_num)
    if num < 0:
      print("Please input more then zero!")
      exit()
    if num > 10000:
      print("Please input below 10000!")
      exit()
    if num % 2 == 0:
      print("Please input not divisible by 2")
      exit()
    elif num % 5 == 0:
      print("Please input not divisible by 5")
      exit()
    else:
      while p % num != 0:
        p += (10 ** i)
        i += 1
      print(i)
      exit()
  except ValueError:
    print("Input is not integer!")
    exit()