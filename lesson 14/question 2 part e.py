vowels = "aeiouAEIOU"

word = input("Enter a word: ")
for i in range(len(word)):
    if vowels.find(word[i]) != -1:
        for j in range(len(vowels)):
            if vowels[j] == word[i]:
                if j + 1 < 5 or j + 1 > 5 and j + 1 <= 9:
                    print(vowels[j+1], end = "")
                elif j == 4:
                    print("a", end = "")
                else:
                    print("A", end = "")
    else:
        print(word[i], end = "")
