userChoice = int(input("Enter 1 for cm to inch or 2 for inch to cm: "))

if userChoice == 1:
  cm = float(input("Enter an amount in cm: "))
  print(f"{cm} cm is {cm/2.54} inch")

if userChoice == 2:
  inch = float(input("Enter an amount in inches"))
  print(f"{inch} inches is {inch*2.54} cm: ")
