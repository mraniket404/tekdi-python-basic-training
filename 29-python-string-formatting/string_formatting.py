# Python String Formatting

# 1. Basic F-string
name = "Aniket"
age = 21

print(f"My name is {name} and I am {age} years old.")


# 2. Decimal formatting
price = 59

print(f"The price is {price:.2f} dollars")


# 3. Direct value formatting
print(f"The price is {95:.2f} dollars")


# 4. Mathematical operation
price = 59
tax = 0.25

print(f"Price with tax: {price + (price * tax)}")


# 5. If-else inside F-string
price = 49

print(f"It is very {'Expensive' if price > 50 else 'Cheap'}")


# 6. Function inside F-string
fruit = "apples"

print(f"I love {fruit.upper()}")


# 7. Thousand separator
price = 59000

print(f"The price is {price:,} dollars")


# 8. format() method
quantity = 3
itemno = 567
price = 49

myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))


# 9. Index numbers
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."

print(myorder.format(quantity, itemno, price))


# 10. Named indexes
myorder = "I have a {carname}, it is a {model}."

print(myorder.format(carname="Ford", model="Mustang"))