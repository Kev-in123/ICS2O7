word = input("Enter a word. Type \"quit\" to quit: ") 
for i in range(len(word)):
    vowel = [i for i in range(len(word)) if "aeiou".find(word[i])!=-1]
greatest = len(vowel)  
greatestword = word  

while word != "quit":
    word = input("Enter a word. Type \"quit\" to quit: ") 
    vowel = [i for i in range(len(word)) if "aeiou".find(word[i])!=-1]
    if len(vowel) > greatest:
        greatest = len(vowel) 
        greatestword = word  
    
print(greatestword)