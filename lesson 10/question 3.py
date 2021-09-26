num1 = int(input("Enter a starting number that is even: "))
print("If the ending number is smaller that the starting number, the ending number will be used as the starting number")
num2 = int(input("Enter an ending number that is even: "))

if num1 % 2 == 0 and num2 % 2 == 0:

  if num1 < num2:
    for i in range(num1, num2+2, 2):
      print(i)

  elif num1 > num2:
    for i in range(num2, num1+2, -2):
      print(i)

else:
  print("One of the numbers passed is not even")
