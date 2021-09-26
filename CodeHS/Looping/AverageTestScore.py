mark = 0
average = 0

for i in range(3):
    mark = mark + float(input("Enter mark: "))
    
average = mark/3
print("Your average mark is: " + str(average))