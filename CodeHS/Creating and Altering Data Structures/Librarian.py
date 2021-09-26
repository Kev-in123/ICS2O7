names_list = [input("Name: ") for i in range(5)]

sorted_last_names = sorted([name.split()[-1] for name in names_list])
print(sorted_last_names)