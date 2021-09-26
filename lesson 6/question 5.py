num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print(f'the sum of {num1} and {num2} is {num1+num2}')
print(f'the difference of {num1} and {num2} is {num1-num2}')
print(f'the product of {num1} and {num2} is {num1*num2}')
if num2 == 0:
  print("Error: division by zero")
else:
  print(f'the quotient of {num1} and {num2} is {num1/num2}')
