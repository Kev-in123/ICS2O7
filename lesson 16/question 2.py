import random

rolls = [random.randint(1, 6) + random.randint(1,6) for i in range(50)]

try:
  interested_roll = int(input("What number are you interested in: "))
except ValueError:
  print("Invalid value try again")
  interested_roll = int(input("What number are you interested in: "))

while 2<interested_roll>12:
  print("Invalid number try again")
  try:
    interested_roll = int(input("What number are you interested in: "))
  except ValueError:
    print("Invalid value try again")
    interested_roll = int(input("What number are you interested in: "))

count_interested = rolls.count(interested_roll)

print(f"The number {interested_roll} appeared {count_interested} time(s)")