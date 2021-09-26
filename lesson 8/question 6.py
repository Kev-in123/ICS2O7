num1 = int(input("Enter a positive number: "))
num2 = int(input("Enter a positive number: "))

while num2 > num1:
  print("Second number must not be larger than the first")
  num1 = int(input("Enter a positive number: "))
  num2 = int(input("Enter a positive number: "))

if num1 % num2 == 0:
  print(f"{num2} is a factor of {num1}")
else:
  print(f"{num2} is not a factor of {num1}")
