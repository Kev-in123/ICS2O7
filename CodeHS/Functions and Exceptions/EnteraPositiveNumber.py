def retrieve_positive_number():
    try:
        num=float(input())
    except ValueError:
        print("Invalid number")
    while num<=0:
        print("Invalid number")
    return num