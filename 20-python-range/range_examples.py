# Python range()


# 1. Range with one argument
print("range(5):")

for number in range(5):
    print(number)


# 2. Range with two arguments
print("range(2, 7):")

for number in range(2, 7):
    print(number)


# 3. Range with three arguments
print("range(2, 10, 2):")

for number in range(2, 10, 2):
    print(number)


# 4. Check range type
numbers = range(10)

print("Type:", type(numbers))


# 5. Print numbers from 10 to 20
print("10 to 20:")

for number in range(10, 21):
    print(number)


# 6. Print odd numbers
print("Odd numbers:")

for number in range(1, 10, 2):
    print(number)


# 7. Print even numbers
print("Even numbers:")

for number in range(2, 11, 2):
    print(number)