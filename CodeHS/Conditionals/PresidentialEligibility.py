age=int(input("Age: "))
birthPlace=str(input("Born in the U.S.? (Yes/No): "))
residency=int(input("Years of Residency: "))

if age>=35 and birthPlace.lower()=="yes" and residency>=24:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")