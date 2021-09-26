x = int(input())
n = int(input())

if n >= 1:
  total = [(x**i) for i in range(n+1)]
  print(sum(total))

else:
  print("Invalid value passed for n")
