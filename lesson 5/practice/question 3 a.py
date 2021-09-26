week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

day = str(input("Which day of the week is it today? "))
if day.lower() in week:
  pass
else:
    print("Invalid input.")
    exit()

print(f"You will take your medicine on a {day} in 28 days.")
