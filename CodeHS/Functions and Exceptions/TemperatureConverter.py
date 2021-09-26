# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!




# Now write your function for converting Fahrenheit to Celsius.

def toF(temp:float):
    return temp*1.8+32



def toC(temp:float):
    return (temp-32)/1.8


# Now change 0C to F:
print(toF(0))

# Change 100C to F:
print(toF(100))

# Change 40F to C:
print(toC(40))

# Change 80F to C:
print(toC(80))