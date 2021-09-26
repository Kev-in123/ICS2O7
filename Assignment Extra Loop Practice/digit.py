count = 0

def count_zeros(number):
  while number > 9:
    count = 0
    if number % 10 == 0:
      count += 1
    number //= 10
  return count

num = int(input("Enter a number: "))

print(f"{num} has {count_zeros(num)} zero(s)")
