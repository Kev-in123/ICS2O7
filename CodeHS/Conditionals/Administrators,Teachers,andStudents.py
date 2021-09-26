user=input("Are you an administrator, teacher, or student?: ")

if user.lower()=="administrator":
    print("Administrators and teachers get keys!")
    
    
elif user.lower()=="teacher":
    print("Administrators and teachers get keys!")
    
elif user.lower()=="student":
    print("Students do not get keys!")
    
else:
    print("You can only be an administrator, teacher, or student!")