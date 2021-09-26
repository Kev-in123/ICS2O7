def factor(num1: float, num2: float):
  if num1 % num2 == 0:
    return f"{num2} is a factor of {num1}"
  else:
    return f"{num2} is not a factor of {num1}"

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(factor(num1, num2))
