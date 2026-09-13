# Python Datetime

import datetime


# 1. Current date and time
now = datetime.datetime.now()

print("Current date and time:", now)


# 2. Current year
print("Year:", now.year)


# 3. Current month
print("Month:", now.month)


# 4. Current day
print("Day:", now.day)


# 5. Current weekday
print("Weekday:", now.strftime("%A"))


# 6. Create a specific date
date = datetime.datetime(2020, 5, 17)

print("Specific date:", date)


# 7. Month name
print("Month name:", date.strftime("%B"))


# 8. Different date formats
print("DD/MM/YYYY:", now.strftime("%d/%m/%Y"))
print("YYYY-MM-DD:", now.strftime("%Y-%m-%d"))


# 9. Time format
print("Time:", now.strftime("%H:%M:%S"))


# 10. 12-hour format
print("12-hour time:", now.strftime("%I:%M %p"))


# 11. Full readable format
print(
    "Readable date:",
    now.strftime("%A, %d %B %Y")
)