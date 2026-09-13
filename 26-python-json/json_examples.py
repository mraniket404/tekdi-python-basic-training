# Python JSON

import json


# 1. JSON string
json_string = '{ "name": "John", "age": 30, "city": "New York" }'


# 2. JSON to Python
python_data = json.loads(json_string)

print("Python data:", python_data)
print("Name:", python_data["name"])
print("Age:", python_data["age"])


# 3. Python dictionary
person = {
    "name": "Aniket",
    "age": 21,
    "city": "Kolhapur"
}


# 4. Python to JSON
json_data = json.dumps(person)

print("JSON data:", json_data)


# 5. Different Python types
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# 6. Nested data
student = {
    "name": "Aniket",
    "age": 21,
    "is_student": True,
    "subjects": [
        "Python",
        "JavaScript",
        "Database"
    ],
    "address": {
        "city": "Kolhapur",
        "country": "India"
    }
}


# 7. Pretty JSON
print("\nPretty JSON:")

print(json.dumps(student, indent=4))


# 8. Sorted keys
print("\nSorted JSON:")

print(json.dumps(student, indent=4, sort_keys=True))