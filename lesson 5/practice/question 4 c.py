ninjaCost = 3.99
truckCost = 8.99
total = (ninjaCost+truckCost)*1.13

balance = float(input("How much money do you have? "))

setOfToys = int(balance//total)
change = balance - setOfToys*total

if change > truckCost:
  change = balance - (setOfToys+1)*truckCost*1.13 - setOfToys*ninjaCost*1.13
  print(f"You can buy toy {setOfToys+1} truck(s) and toy {setOfToys} ninja(s) with {balance:.2f} and have ${change:.2f} left")
elif change > ninjaCost:
  change = balance - (setOfToys+1)*ninjaCost*1.13 - setOfToys*truckCost*1.13
  print(f"You can buy toy {setOfToys} truck(s) and toy {setOfToys+1} ninja(s) with {balance:.2f} and have ${change:.2f} left")
else:
  print(f"You can buy toy {setOfToys} truck(s) and toy {setOfToys} ninja(s) with {balance:.2f} and have ${change:.2f} left")

