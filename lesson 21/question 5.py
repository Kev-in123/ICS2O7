import random

def replace_a(string):
  result = ["aa" if i=="a" else i for i in string] #can also do: result=word.replace("a","aa")
  return "".join(result)

def replace_b(string):
  result = ["c" if i=="b" else i for i in string] #can also do: result=string.replace("b","c")
  return "".join(result)

def insert_c(string):
  place = random.randint(0, len(string))
  return f"{string[:place]}c{string[place:]}"

word = input("Enter some text: ")
functions = [replace_a(word), replace_b(word), insert_c(word)]
for i in range(5):
  print(random.choice(functions))

