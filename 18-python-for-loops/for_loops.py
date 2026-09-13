# Python For Loops


# 1. Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# 2. Loop through a string
for character in "banana":
    print(character)


# 3. Break statement
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("Break:", fruit)

    if fruit == "banana":
        break


# 4. Continue statement
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue

    print("Continue:", fruit)


# 5. range()
for number in range(6):
    print("Range:", number)


# 6. range(start, stop)
for number in range(2, 6):
    print("Start-stop:", number)


# 7. range(start, stop, step)
for number in range(2, 15, 3):
    print("Step:", number)


# 8. For loop with else
for number in range(3):
    print("Else loop:", number)
else:
    print("Loop finished")


# 9. Nested loops
adjectives = ["red", "big"]
fruits = ["apple", "banana"]

for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)


# 10. Pass statement
for number in [0, 1, 2]:
    pass