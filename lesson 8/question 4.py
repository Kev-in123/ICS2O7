while True:
  num = int(input("Enter a positive integer (0 or a negative value to exit): "))
  if num <= 0:
    break

    if num > 0:
      for i in range(1, 11):
        print(i*num, end = " ")
      print()

print("End of program")

