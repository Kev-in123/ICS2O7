counter = 0

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if not num2 > num1:
  print("The second number nust be larger than the first >:(")
  raise SystemExit

for i in range(num1, num2):
  counter += i
  i = counter

print(i)

