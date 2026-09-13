# Python Try Except

# 1. Basic try-except
try:
    print(x)
except:
    print("An exception occurred")


# 2. Specific exception
try:
    print(y)
except NameError:
    print("Variable y is not defined")
except:
    print("Something else went wrong")


# 3. Else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# 4. Finally
try:
    print(z)
except:
    print("Something went wrong")
finally:
    print("Try-except is finished")


# 5. Raise
age = -5

if age < 0:
    raise Exception("Age cannot be negative")