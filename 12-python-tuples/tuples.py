# Python Tuples

# Create a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Duplicate values
fruits = ("apple", "banana", "apple", "cherry")
print(fruits)

# Tuple length
print(len(fruits))

# One-item tuple
one_item = ("apple",)
print(one_item)
print(type(one_item))

# Not a tuple
not_tuple = ("apple")
print(type(not_tuple))

# Empty tuple
empty_tuple = ()
print(type(empty_tuple))

# Different data types
mixed_tuple = ("Aniket", 21, True, 5.8)
print(mixed_tuple)

# Check type
print(type(fruits))

# tuple() constructor
new_tuple = tuple(("apple", "banana", "cherry"))
print(new_tuple)