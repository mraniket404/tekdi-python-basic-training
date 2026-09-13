# Python Lists

# Create a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# List indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Change an item
fruits[0] = "mango"
print(fruits)

# Duplicate values
fruits = ["apple", "banana", "apple", "cherry"]
print(fruits)

# List length
print(len(fruits))

# Different data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9]
list3 = [True, False, True]
list4 = ["Aniket", 21, True, 5.8]

print(list1)
print(list2)
print(list3)
print(list4)

# Check data type
print(type(fruits))

# list() constructor
new_list = list(("apple", "banana", "cherry"))
print(new_list)