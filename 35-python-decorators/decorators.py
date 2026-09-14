# Python Decorators


# 1. Basic decorator
def my_decorator(function):

    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()


# 2. Decorator with argument
def welcome_decorator(function):

    def wrapper(name):
        print("Starting function...")
        function(name)
        print("Function finished.")

    return wrapper


@welcome_decorator
def welcome(name):
    print(f"Welcome, {name}!")


welcome("Aniket")


# 3. Decorator with calculation
def calculation_decorator(function):

    def wrapper(a, b):
        print("Calculating...")
        result = function(a, b)
        print("Result:", result)

    return wrapper


@calculation_decorator
def add(a, b):
    return a + b


add(10, 20)