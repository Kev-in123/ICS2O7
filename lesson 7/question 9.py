nums = []

num = int(input("Enter some positive integers (0 or a negative number to exit): "))

while True:
  if num > 0:
    nums.append(num)
    num = int(input("Enter some positive integers (0 or a negative number to exit): "))
  else:
    break

try:
   print(f"The range is {max(nums)-min(nums)}")

except:
   print("No range")
