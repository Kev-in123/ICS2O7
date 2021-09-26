week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

day = str(input("Which day of the week is it today? "))
if day.lower() in week:
  pass
else:
    print("Invalid input.")
    exit()

how_often = int(input("How often do you take your medicine? "))

print(f"You will take your medicine on a {day} in {how_often*7} days.")
