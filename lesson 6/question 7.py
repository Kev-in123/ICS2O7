num1 = float(input("Number 1: "))
num2 = float(input("Wumber 2: "))
operation = input("Which operation (+,-,/,*): ")

if operation == "+":
  print(f"The sum is {num1 + num2}")
  
if operation == "-":
  print(f"The difference is {num1 - num2}")
  
if operation == "/":
  if num2 != 0:
    print(f"The quotient is {num1 / num2}")
  else:
    print("Cannot divide any number by zero!")
    
if operation == "*":
  print(f"The product is {num1 * num2}")
