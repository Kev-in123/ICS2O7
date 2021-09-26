def remove(word, char):
  word = [c for c in word if c != char] #can also do: word=word.replace(char,"")
  return "".join(word)


print(remove("spaghetti", "t"))