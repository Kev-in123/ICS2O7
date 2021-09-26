def glue(word1, word2):
  return word1 + word2

def reverse(word):
  return word[::-1]

def machine(word1, word2, word3):
  return glue(reverse(glue(word1, word2)), word3)

word1, word2, word3 = str(input("Enter 3 words seperated by spaces: ")).split()
print(machine(word1, word2, word3))
