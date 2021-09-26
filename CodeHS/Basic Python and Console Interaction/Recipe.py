"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""

# Write program here...
ingredient_1 = str(input("Enter ingredient 1: "))
ounces_1 = float(input(f"Ounces of {ingredient_1}: "))
ingredient_2 = str(input("Enter ingredient 2: "))
ounces_2 = float(input(f"Ounces of {ingredient_2}: "))
ingredient_3 = str(input("Enter ingredient 3: "))
ounces_3 = float(input(f"Ounces of {ingredient_3}: "))
servings = int(input("Number of servings: "))
ounces_1*=servings
ounces_2*=servings
ounces_3*=servings


print(f"Total ounces of {ingredient_1}: {ounces_1}")
print(f"Total ounces of {ingredient_2}: {ounces_2}")
print(f"Total ounces of {ingredient_3}: {ounces_3}")