
def rainy():
    print("On a rainy day, galoshes are appropriate footwear.")
    
def snowy():
    print("On a snowy day, boots are appropriate footwear.")
    
def sunny():
    print("On a sunny day, sandals are appropriate footwear.")
    
weather = input("What is the weather? (sunny, rainy, snowy): ")

if weather == "rainy":
    rainy()
elif weather == "snowy":
    snowy()
elif weather == "sunny":
    sunny()
else:
    print("Invalid option.")