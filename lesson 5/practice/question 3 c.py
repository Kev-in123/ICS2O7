week = {
    "monday":1,
    "tuesday":2,
    "wednesday":3,
    "thursday":4,
    "friday":5,
    "saturday":6,
    "sunday":7
        }

day = str(input("Which day of the week is it today? "))
if day.lower() in week:
  day = week[day]
else:
    print("Invalid input.")
    exit()

interested_day = str(input("Which day of the week are you interested in to repeat your medicine? "))
if interested_day.lower() in week:
    interested_day_ = week[interested_day]
else:
    print("Invalid input.")
    exit()

how_often = int(input("How often do you take your medicine (in days)? "))

next_medication = int(0) 
if (interested_day_ - day > 0):
    next_medication = (interested_day_ - day) * how_often
else:
    next_medication = (interested_day_ - day +7) * how_often

print(f"You will take your medicine on a {interested_day} in {next_medication} day(s).")
