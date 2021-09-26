import math

num1 = int(input("Enter 2 numbers and find their LCM: "))
num2 = int(input())

lcmFunc = lambda x, y: (x*y)//math.gcd(x, y)

lcm = lcmFunc(num1, num2)

print(f"The lcm of {num1} and {num2} is {lcm}")

