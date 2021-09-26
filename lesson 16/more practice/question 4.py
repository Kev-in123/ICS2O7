inventory = {}

items = [input("Enter an item: ") for i in range(10)]
try:
  amounts = [int(input(f"How many {i}s do you have: ")) for i in items]  
except  ValueError:
  print("Invalid amount entered")
  exit()

for item in items:
  for amount in amounts:
    inventory[item] = amount
    amounts.remove(amount)
    break 

item = input("What item do you wnat to know the amount of: ")
print(f"You have {inventory[item]} {item}(s)")