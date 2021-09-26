import random

nums = [(random.uniform(50, 60)) for i in range(20)]

for num in nums:
  print(f"number {nums.index(num) + 1}: {num}")
