# Using our custom module

import mymodule


# Use function from module
mymodule.greeting("Aniket")


# Use another function
result = mymodule.add(10, 20)
print("Addition:", result)


# Access variable from module
print("Name:", mymodule.person1["name"])
print("Age:", mymodule.person1["age"])


# Module alias
import mymodule as mx

print("Country:", mx.person1["country"])


# Import specific function
from mymodule import greeting

greeting("Rahul")


# Check available names
print(dir(mymodule))