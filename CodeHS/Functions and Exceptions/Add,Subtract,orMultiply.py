num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?:"))
op = input("Choose an operation (add, subtract, multiply): ")
def add():
    print(f"{num1} + {num2} = {num1 + num2}")

def sub():
    print(f"{num1} - {num2} = {num1 - num2}")


def multiply():
    print(f"{num1} * {num2} = {num1 * num2}")



if op == "add":
    add()
elif op == "subtract":
    sub()
elif op == "multiply":
    multiply()
else:
    print("Invalid")