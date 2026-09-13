# Python Operators

# Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Power:", a ** b)
print("Floor Division:", a // b)

# Assignment Operator
x = 10
x += 5
print("Assignment:", x)

# Comparison Operators
print("Greater:", a > b)
print("Equal:", a == b)
print("Not Equal:", a != b)

# Logical Operators
print("AND:", a > 5 and b < 5)
print("OR:", a < 5 or b < 5)
print("NOT:", not(a > 5))

# Membership Operators
fruits = ["apple", "banana", "cherry"]

print("apple in fruits:", "apple" in fruits)
print("mango not in fruits:", "mango" not in fruits)

# Identity Operators
list1 = [1, 2, 3]
list2 = list1

print("Same object:", list1 is list2)