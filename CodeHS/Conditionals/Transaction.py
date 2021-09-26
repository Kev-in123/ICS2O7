# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.

balance=1000
userInput=str(input("Deposit or withdrawal: "))
if userInput.lower()=="withdrawal":
    userInput2=float(input("Enter amount: "))
    if userInput2>1000:
        print("You cannot have a negative balance!")
        
    else:
        balance-=userInput2
        print(f"Final balance: {balance}")
        
        
elif userInput.lower()=="deposit":
    userInput2=float(input("Enter amount: "))
    balance+=userInput2
    print(f"Final balance: {balance}")

else:
    print("Invalid transaction.")