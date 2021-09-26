def toF(temp:float):
    return temp*1.8+32

def toC(temp:float):
    return (temp-32)/1.8

try:
    num=float(input())
    toF(num)
except ValueError:
    print("Invalid")
    
    
try:
    num=float(input())
    toC(num)
except ValueError:
    print("Invalid")