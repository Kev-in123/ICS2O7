def isPalindrome(word):
  if word[::-1] == word:
    return True
  else:
    return False

print(isPalindrome("racecar"))
print(isPalindrome("paper"))