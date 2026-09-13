# Python Sets

# Create a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Duplicate values
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

# True and 1 are considered the same
myset = {"apple", "banana", True, 1, 2}
print(myset)

# False and 0 are considered the same
myset2 = {"apple", "banana", False, True, 0}
print(myset2)

# Check type
print(type(fruits))

# Number of items
print(len(fruits))