pos = []
neg = []

num = int(input("Enter a positive/negative number (0 to exit) "))
while True:
  if num == 0:
    break
    
  elif num > 0:
    pos.append(num)
    num = int(input("Enter a positive/negative number (0 to exit) "))
 
  elif num < 0:
    neg.append(num)
    num = int(input("Enter a positive/negative number (0 to exit) "))

print(f"The count of the positive numbers is {len(pos)}\nthe sum of the positive numbers is {sum(pos)}\nthe mean of the positive numbers is {sum(pos)/len(pos)}")
print(f"The count of the negative numbers is {len(neg)}\nthe sum of the negative numbers is {sum(neg)}\nthe mean of the negative numbers is {sum(neg)/len(neg)}")
