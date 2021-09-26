def triangle(rows):
  k = rows - 1
  for i in range(0, rows):
    for j in range(0, k):
      print(end = " ")
    k -= 1
    for j in range(0, i+1):
      print(i + 1, end = "")
    print()

triangle(5)