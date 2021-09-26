num1 = int(input("Enter a starting number: "))
num2 = int(input("Enter an ending number: "))
step = int(input("Enter the increment value: "))

if num1 < num2:
  for i in range(num1, num2 + 1, step):
    print(i)

elif num1 > num2:
  print("Invalid input")
