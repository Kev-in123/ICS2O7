word = input("Enter a word: ")
for char in word:
    if not char.isdigit():
        print(char, end = "")