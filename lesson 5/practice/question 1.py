target = int(input("Enter a target nuber: "))

totalNum = [float(input("Enter a number: ")) for i in range(5)]

largerNum = [num for num in totalNum if num > target]

print(f"There are/is {len(largerNum)} larger number(s) than {target}")
