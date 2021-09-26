my_list = []
for i in range(5):
    new_number = int(input("Number: "))
    my_list.append(new_number)
    print(my_list)
print("Sum: " + str(sum(my_list)))