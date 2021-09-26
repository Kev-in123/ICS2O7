lastnames = [str(input("Enter your last name: ")) for i in range(3)]

for lastname in lastnames:

  lastname = lastname.lower()
  if 97 <= ord(lastname[0]) <= 104:
    print(f"{lastname} You are in group 1")

  elif 105 <= ord(lastname[0]) <= 122 :
    print(f"{lastname} You are in group 2")
     
