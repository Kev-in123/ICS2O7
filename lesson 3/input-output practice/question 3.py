# 1

price = float(input("What is the price of the book? "))

shippingcost = 2.5 + 0.55 * (60 - 1) 
total = 0.6 * (price * 60) + shippingcost 

print(f'The total cost for 60 copies with shipping and 40% discount is: {int(total)} dollars and {str(round(total, 2))[-2:]} cents.')


# 2
amount = int(input("How many books would you like to order: ")) 

shippingcost = 2.5 + 0.55*(amount - 1)
total = 0.6 * (price * amount) + shippingcost

print(f'The total cost for 60 copies with shipping and 40% discount is: {int(total)} dollars and {str(round(total, 2))[-2:]} cents.') # print
