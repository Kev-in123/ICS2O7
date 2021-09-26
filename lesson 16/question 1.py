daily_high = [float(input(f"Enter the highest temprature for day {i+1}: ")) for i in range(10)]
print(daily_high[::-1])
average = sum(daily_high) / len(daily_high)
print(f"The average daily high is {average}")
print(f"The highest daily high is {max(daily_high)}")
print(f"The lowest daily high is {min(daily_high)}")
