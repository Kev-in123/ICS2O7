word = input("Enter a word: ")

for char in word:
  print(char)

print("----------------------------------")

reversed_word = word[::-1]
for char in reversed_word:
  print(char)
print("----------------------------------")

first_last_exchanged = word[-1] + word[1:-1] + word[0]
print(first_last_exchanged)
print("----------------------------------")

half = int(len(word)/2)
print(word[half:] + word[:half])
print("----------------------------------")

d_replaced = word.replace('d','D')
print(d_replaced)
print("----------------------------------")

a_replaced = word.replace('a','')
print(a_replaced)