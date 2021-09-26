for i in range(3):
    category=input("Enter a category: ")
    res=f"{category}: "
    for j in range(3):
        something=input("Enter something in that category: ")
        res+=f"{something} "
    print(res)