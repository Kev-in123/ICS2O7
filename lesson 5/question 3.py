num = int(input("Enter a positive number: "))
if num <= 0:
  print("The number must be positive")

elif not(num <= 0) and num % 2 == 0:
  print("It's even")

elif not(num <= 0) and num % 2 != 0:
  print("It's odd")

