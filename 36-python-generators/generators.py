# Python Generators


# 1. Basic generator
def my_generator(n):
    value = 0

    while value < n:
        yield value
        value += 1


print("Basic generator:")

for value in my_generator(5):
    print(value)


# 2. Generator with next()
generator = my_generator(3)

print("\nUsing next():")
print(next(generator))
print(next(generator))
print(next(generator))


# 3. Generator expression
squares_generator = (i * i for i in range(5))

print("\nSquares:")

for i in squares_generator:
    print(i)


# 4. Power of 2 generator
def power_of_two(max_value):
    n = 0

    while n < max_value:
        yield 2 ** n
        n += 1


print("\nPowers of 2:")

for value in power_of_two(6):
    print(value)


# 5. Generator pipeline
def fibonacci_numbers(nums):
    x, y = 0, 1

    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


result = sum(square(fibonacci_numbers(10)))

print("\nSum of Fibonacci squares:", result)