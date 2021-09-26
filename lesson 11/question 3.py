import random
ran_nums = [random.randint(1,6) for i in range(20)]
for num in range(len(ran_nums)):
  print(f"number {num + 1}: {ran_nums[num]}")
  
for num in range(1, 7):
  occurrences = ran_nums.count(num)
  print(f"occurrences of {num}: {occurrences}")
  
most_occurrences = max(ran_nums, key = ran_nums.count)
print(f"The most common occurrence was: {most_occurrences}")

