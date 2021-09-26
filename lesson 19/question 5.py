def double(num):
  while num <= 100:
    num *= 2
  return num
  
num = int(input("Enter an integer: "))
print(double(num))