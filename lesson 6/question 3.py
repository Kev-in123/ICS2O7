loan = float(input("How much do you have on loan? "))
date = input("I the loan monthly or anually? ")
percent = float(input("What is the percentage? "))

decpercent = percent/100

if date == "monthly":
    print(f"{decpercent*loan*12}")
elif date == "anually":
    print(f"{decpercent*loan}")
else:
    print("you did not enter a valid input")
