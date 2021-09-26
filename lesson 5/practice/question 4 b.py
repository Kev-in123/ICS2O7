ninjaCost = 3.99
truckCost = 8.99

balance = float(input("How much money do you have? "))
prefrence = str(input("Which toy do you prefer? ninja or truck? "))

if prefrence.lower() == "ninja":
  totalNinja = balance//ninjaCost
  change = balance-totalNinja*ninjaCost
  print(f"You can buy {totalNinja} toy ninja(s) and have ${change:.2f} change")

elif prefrence.lower() == "truck":
  totalTruck = balance//truckCost
  change = balance-totalTruck*truckCost
  print(f"You can buy {totalTruck} toy trucks(s) and have ${change:.2f} change")
