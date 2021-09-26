def calculate_area(side_length=10):
    print(f"The area of a square with sides of length {side_length} is {side_length**2}.")

    
length=int(input("Enter side length: "))
if length<=0:
    calculate_area(10)
else:
    calculate_area(length)