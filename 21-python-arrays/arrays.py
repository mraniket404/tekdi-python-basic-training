# Python Arrays
# Python uses Lists as basic arrays


# 1. Create an array/list
cars = ["Ford", "Volvo", "BMW"]

print("Cars:", cars)


# 2. Access elements
print("First car:", cars[0])
print("Second car:", cars[1])


# 3. Modify an element
cars[0] = "Toyota"

print("After modification:", cars)


# 4. Length
print("Length:", len(cars))


# 5. Loop through array
print("All cars:")

for car in cars:
    print(car)


# 6. Add element
cars.append("Honda")

print("After append:", cars)


# 7. Insert element
cars.insert(1, "Audi")

print("After insert:", cars)


# 8. Remove using pop
cars.pop(2)

print("After pop:", cars)


# 9. Remove using remove
cars.remove("Honda")

print("After remove:", cars)


# 10. Count
numbers = [10, 20, 10, 30, 10]

print("Count of 10:", numbers.count(10))


# 11. Index
print("Index of 20:", numbers.index(20))


# 12. Sort
numbers.sort()

print("Sorted numbers:", numbers)


# 13. Reverse
numbers.reverse()

print("Reversed numbers:", numbers)


# 14. Copy
numbers_copy = numbers.copy()

print("Copied list:", numbers_copy)