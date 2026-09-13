# Python Booleans

# Boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

# If and else
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# bool() with values
print(bool("Hello"))
print(bool(15))

# False values
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))

# Function returning Boolean
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

# isinstance()
x = 200
print(isinstance(x, int))

# Exercise
print(5 > 3)