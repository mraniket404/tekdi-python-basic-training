# Python None

# 1. None value
x = None

print("Value:", x)
print("Type:", type(x))


# 2. Compare with None
result = None

if result is None:
    print("No result yet")
else:
    print("Result is ready")


# 3. is not None
result = "Success"

if result is not None:
    print("Result is ready")
else:
    print("No result yet")


# 4. Boolean value of None
print("Boolean value:", bool(None))


# 5. Function returning None
def myfunc():
    x = 5

x = myfunc()

print("Function result:", x)