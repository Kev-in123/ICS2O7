ninjaCost = 3.99
truckCost = 8.99

ninjaAmt = int(input("How many ninjas do you want to buy? "))
truckAmt = int(input("How many trucks do you want to buy? "))

total = (ninjaAmt*ninjaCost+truckAmt*truckCost) * 1.13

print(f"To buy {ninjaAmt} ninja(s) and {truckAmt} truck(s) you will need to pay {total}")
