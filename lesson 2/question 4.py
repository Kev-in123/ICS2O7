lastDigit = 0

num = int(input("Enter a number: "))
if 10 <= num <= 99:
  lastDigit = num % 10
  print(lastDigit) 
else:
  print('Must be a 2 digit number')
