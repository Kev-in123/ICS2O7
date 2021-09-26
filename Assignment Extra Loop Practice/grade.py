target = float(input("Enter a target grade: "))

grades = [float(input("Enter a grade: ")) for i in range(5)]

above = [grade for grade in grades if grade > target]

if len(above) == 1:
  print(f"There is {len(above)} grade above the target grade: {target}\n{((len(above)/len(grades))*100):.0f}% of grades are above the target grade")
else:
  print(f"There are {len(above)} grades above the target grade: {target}\n{((len(above)/len(grades))*100):.0f}% of grades are above the target grade")
