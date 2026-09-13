# Python Match Statement

# 1. Basic match
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


# 2. Default case
day = 10

match day:
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# 3. Combine values using |
day = 3

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")


# 4. Match with if guard
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("Weekday in May")
    case _:
        print("No match")