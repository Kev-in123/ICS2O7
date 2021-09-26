students_per_group = 0

students = int(input("How many students are in the class: "))
groups = int(input("How many students per group: "))

students_per_group = students // groups 

if students % groups == 0:
  print(f'There are {students_per_group} groups of {groups}')

else:
  print(f'There are {students_per_group-students % groups} groups of {groups} and {students % groups} groups of {groups + 1}') 
