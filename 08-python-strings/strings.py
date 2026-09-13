# Python Strings

# Single and double quotes
print("Hello")
print('Hello')

# Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# String variable
name = "Aniket"
print(name)

# Multiline string
text = """Hello
I am learning Python
at Tekdi Technologies"""

print(text)

# String indexing
a = "Hello"
print(a[1])

# Loop through string
for x in "banana":
    print(x)

# String length
print(len(a))

# Check string
txt = "The best things in life are free!"

print("free" in txt)

if "free" in txt:
    print("Yes, free is present.")

# Check NOT
print("expensive" not in txt)

if "expensive" not in txt:
    print("No, expensive is NOT present.")

# Exercise
x = "Welcome"
print(x[3])