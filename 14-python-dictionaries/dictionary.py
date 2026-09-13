# Python Dictionaries

# Create a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)


# Access dictionary value using key
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])


# Change a value
thisdict["year"] = 2020

print(thisdict)


# Add a new item
thisdict["color"] = "Red"

print(thisdict)


# Duplicate key
duplicate_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(duplicate_dict)


# Dictionary length
print(len(thisdict))


# Different data types
student = {
    "name": "Aniket",
    "age": 21,
    "is_student": True,
    "marks": [80, 85, 90]
}

print(student)


# Access different values
print(student["name"])
print(student["age"])
print(student["is_student"])
print(student["marks"])


# Check data type
print(type(student))


# dict() constructor
person = dict(
    name="John",
    age=36,
    country="Norway"
)

print(person)


# Exercise
x = {
    "type": "fruit",
    "name": "banana"
}

print(x)