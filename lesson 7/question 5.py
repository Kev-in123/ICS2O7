num = float(input("Enter a number (0 to exit): "))

while True:
  if num == 0:
    break

  else:
    print(num*-1)
    num = float(input("Enter a number (0 to exit): "))

print("End of program")
