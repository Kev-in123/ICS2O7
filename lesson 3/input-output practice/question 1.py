mark1, mark2, mark3 = str(input("Enter 3 marks: ")).split() 
course = str(input("Enter a course name: "))

print(f"Your {course} average is {(float(mark1) + float(mark2) + float(mark3)) / 3 :.2f}") 
