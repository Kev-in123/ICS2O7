def triangle(rows):
  spaces = rows
  for i in range(0, rows*2, 2):
    for j in range(0, spaces):
      print(end = " ")
    spaces -= 1
    for j in range(0, i + 1):
      print("$", end = "")
    print()

triangle(5)