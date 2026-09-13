# Python Lambda

# 1. Single argument
x = lambda a: a + 10
print("Add 10:", x(5))


# 2. Two arguments
x = lambda a, b: a * b
print("Multiply:", x(5, 6))


# 3. Three arguments
x = lambda a, b, c: a + b + c
print("Sum:", x(5, 6, 2))


# 4. Lambda inside a function
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print("Double:", mydoubler(11))
print("Triple:", mytripler(11))


# 5. Lambda with map()
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))

print("Doubled:", doubled)


# 6. Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Odd numbers:", odd_numbers)


# 7. Lambda with sorted()
students = [
    ("Emil", 25),
    ("Tobias", 22),
    ("Linus", 28)
]

sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted students:", sorted_students)


# 8. Sort by string length
words = ["apple", "pie", "banana", "cherry"]

sorted_words = sorted(words, key=lambda x: len(x))

print("Sorted words:", sorted_words)