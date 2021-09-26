age=int(input("Age: "))
birthPlace=str(input("Born in the U.S.? (Yes/No): "))
residency=int(input("Years of Residency: "))

if age>=35 and birthPlace=="Yes" and residency>=14:
    print("You are eligible to run for president!")

else:
    print("You are not eligible to run for president.")
    if age<35:
        print("You are too young to run for president. You must be at least 35 years old.")
    if birthPlace!="Yes":
        print("You are not born in th U.S. You must be born in the U.S. to run for president.")
    if residency<14:
        print("You have not been a resident for long enough. You must be a a resident of the U.S. for 14 years.")