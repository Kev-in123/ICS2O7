num1 = int(input("Enter 2 numbers to find their average (enter 0 twice to exit):\n"))
num2 = int(input())

while (num1 and num2) != 0:
  if (num1 and num2) == 0:
    break
  print(f"The average of {num1} and {num2} is {(num1+num2)/2}")
  num1 = int(input("Enter 2 numbers to find their average (enter 0 twice to exit):\n"))
  num2 = int(input())

print("End of program")
