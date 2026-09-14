# Python List Comprehension

# 1. Double numbers
numbers = [1, 2, 3, 4]

doubled_numbers = [num * 2 for num in numbers]

print("Doubled:", doubled_numbers)


# 2. Square numbers
numbers = [1, 2, 3, 4, 5]

square_numbers = [num * num for num in numbers]

print("Squares:", square_numbers)


# 3. Even numbers
even_numbers = [
    num for num in range(1, 10)
    if num % 2 == 0
]

print("Even numbers:", even_numbers)


# 4. Odd numbers
odd_numbers = [
    num for num in range(1, 10)
    if num % 2 != 0
]

print("Odd numbers:", odd_numbers)


# 5. Vowels from string
word = "Python"
vowels = "aeiou"

result = [
    char for char in word
    if char in vowels
]

print("Vowels:", result)


# 6. Convert words to uppercase
words = ["apple", "banana", "cherry"]

uppercase_words = [word.upper() for word in words]

print("Uppercase:", uppercase_words)