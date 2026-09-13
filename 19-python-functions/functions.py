# Python Functions


# 1. Basic function
def greet():
    print("Hello from a function")


greet()


# 2. Calling function multiple times
greet()
greet()


# 3. Function with parameter
def greet_user(name):
    print("Hello", name)


greet_user("Aniket")
greet_user("Rahul")


# 4. Function with two parameters
def add_numbers(a, b):
    print(a + b)


add_numbers(10, 20)
add_numbers(5, 15)


# 5. Function with return
def add(a, b):
    return a + b


result = add(10, 20)
print("Result:", result)


# 6. Reusable temperature conversion function
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("Celsius:", fahrenheit_to_celsius(77))
print("Celsius:", fahrenheit_to_celsius(95))
print("Celsius:", fahrenheit_to_celsius(50))


# 7. Function returning a string
def get_greeting():
    return "Hello from a function"


message = get_greeting()
print(message)


# 8. Function without return
def say_hello():
    print("Hello")


value = say_hello()
print("Returned value:", value)


# 9. Pass statement
def future_function():
    pass