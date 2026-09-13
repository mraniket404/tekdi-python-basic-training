# Python While Loops


# 1. Basic while loop
i = 1

while i < 6:
    print(i)
    i += 1


# 2. Break statement
i = 1

while i < 6:
    print("Break:", i)

    if i == 3:
        break

    i += 1


# 3. Continue statement
i = 0

while i < 6:
    i += 1

    if i == 3:
        continue

    print("Continue:", i)


# 4. While loop with else
i = 1

while i < 4:
    print("Else loop:", i)
    i += 1
else:
    print("Loop finished")