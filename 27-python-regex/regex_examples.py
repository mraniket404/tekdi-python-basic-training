# Python RegEx

import re

txt = "The rain in Spain"

# 1. findall()
x = re.findall("ai", txt)
print("findall:", x)

# 2. search()
x = re.search("\s", txt)
print("First whitespace position:", x.start())

# 3. split()
x = re.split("\s", txt)
print("split:", x)

# 4. sub()
x = re.sub("\s", "9", txt)
print("sub:", x)

# 5. Digits
text = "My age is 21"
x = re.findall(r"\d", text)
print("Digits:", x)

# 6. Match object
x = re.search(r"\bS\w+", txt)

print("Matched text:", x.group())
print("Original string:", x.string)
print("Position:", x.span())