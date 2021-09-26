food_1 = str(input("What is the first food item you bought: "))
price_1 = float(input("How much did it cost: "))
amt_1 = int(input("How many did you buy: "))

food_2 = str(input("What is the first food item you bought: "))
price_2 = float(input("How much did it cost: "))
amt_2 = int(input("How many did you buy: "))

food_3 = str(input("What is the first food item you bought: "))
price_3 = float(input("How much did it cost: "))
amt_3 = int(input("How many did you buy: "))

totalBill = (price_1 * amt_1) + (price_2 * amt_2) + (price_3 * amt_3)

print(f"The total bill is {totalBill}")