word = input("Enter a word: ")

for char in word:
    if not char.isalpha():
        print(char, end = "")
        