def pattern(rows):
  for i in range(rows , 0, -2):
    for j in range(0, i):
      print("*", end = "")
    print()

pattern(10)