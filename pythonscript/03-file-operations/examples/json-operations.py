#!/usr/bin/env python3
"""
Example 3: JSON Operations
Demonstrate JSON file operations
"""

import json

# Writing JSON
print("=== Writing JSON ===")
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC',
    'hobbies': ['reading', 'coding', 'traveling']
}

with open('person.json', 'w') as f:
    json.dump(data, f, indent=2)

print("JSON file created!")

# Reading JSON
print("\n=== Reading JSON ===")
with open('person.json', 'r') as f:
    loaded_data = json.load(f)
    print(f"Name: {loaded_data['name']}")
    print(f"Age: {loaded_data['age']}")
    print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")

# JSON string operations
print("\n=== JSON String Operations ===")
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# Parse JSON string
parsed = json.loads(json_string)
print(f"\nParsed name: {parsed['name']}")

# Nested JSON
print("\n=== Nested JSON ===")
nested_data = {
    'company': {
        'name': 'Tech Corp',
        'employees': [
            {'name': 'Alice', 'role': 'Developer'},
            {'name': 'Bob', 'role': 'Designer'}
        ]
    }
}

with open('company.json', 'w') as f:
    json.dump(nested_data, f, indent=2)

print("Nested JSON file created!")
