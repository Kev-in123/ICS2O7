classSize = int(input("how many students are in the class?"))
groupSize = int(input("how many people per group? "))

groupNumber = classSize//groupSize
extra = classSize % groupSize

if extra == 0:
    print(f"all groups will be the same having {int(classSize/groupSize)} groups of {groupSize}")
else:
    if extra > groupNumber:
        print(f"there will be {groupNumber - extra % groupNumber} group(s) of {groupSize + (extra//groupNumber)} and  {extra % groupNumber} group(s) of {groupSize + (extra//groupNumber) + 1}")
    else:        
        print(f"there will be {(classSize//groupSize) - extra} group(s) of {groupSize} and {extra} group(s) of {groupSize + 1}")
