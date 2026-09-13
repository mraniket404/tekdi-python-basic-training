# Python Built-in Functions

# Basic functions
name = "Aniket"
numbers = [10, 20, 30, 40, 50]

print("Name:", name)
print("Type:", type(name))
print("Length:", len(name))

# Type conversion
age = "21"

print("Integer:", int(age))
print("Float:", float(age))
print("String:", str(100))
print("Boolean:", bool(1))

# Math functions
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Absolute:", abs(-25))
print("Rounded:", round(3.14159, 2))

# Sequence functions
print("Range:", list(range(5)))
print("Sorted:", sorted([50, 10, 30, 20, 40]))

# all()
print("All:", all([True, True, True]))

# any()
print("Any:", any([False, False, True]))

# enumerate()
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip()
names = ["Aniket", "Rahul", "Amit"]
ages = [21, 22, 20]

for name, age in zip(names, ages):
    print(name, age)