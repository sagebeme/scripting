#!/usr/bin/env python3
"""
Solution: Exercise 3 - JSON Operations
Complete solution for the exercise
"""

import json
import os

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 3 - JSON Operations")
print("=" * 60)

json_file = 'data.json'

# Task 1: Write dictionary to JSON file
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
with open(json_file, 'w') as f:
    json.dump(data, f)
print("1. JSON file created")

# Task 2: Read JSON file
print("\n2. Reading JSON file:")
with open(json_file, 'r') as f:
    loaded_data = json.load(f)
print(f"   {loaded_data}")

# Task 3: Pretty print JSON
print("\n3. Pretty print JSON:")
with open('pretty.json', 'w') as f:
    json.dump(data, f, indent=4)
print("   Created pretty.json with indentation")

# Task 4: Read JSON string
print("\n4. Parsing JSON string:")
json_string = '{"name": "Bob", "age": 25}'
parsed = json.loads(json_string)
print(f"   {parsed}")

# Task 5: Convert Python object to JSON string
print("\n5. Converting to JSON string:")
person = {'name': 'Charlie', 'age': 35}
json_str = json.dumps(person)
print(f"   {json_str}")

# Task 6: Handle JSON errors
print("\n6. Handling JSON errors:")
invalid_json = "{'name': 'Invalid'}"  # Invalid JSON (uses single quotes)
try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"   Error caught: {e}")

# Task 7: Read nested JSON
print("\n7. Working with nested JSON:")
nested_data = {
    'person': {
        'name': 'David',
        'details': {
            'age': 40,
            'city': 'Boston'
        }
    }
}
with open('nested.json', 'w') as f:
    json.dump(nested_data, f, indent=2)
with open('nested.json', 'r') as f:
    loaded_nested = json.load(f)
print(f"   Name: {loaded_nested['person']['name']}")
print(f"   Age: {loaded_nested['person']['details']['age']}")

# Task 8: Update JSON file
print("\n8. Updating JSON file:")
with open(json_file, 'r') as f:
    data = json.load(f)
data['age'] = 31  # Update age
data['email'] = 'alice@example.com'  # Add new field
with open(json_file, 'w') as f:
    json.dump(data, f, indent=2)
print(f"   Updated: {data}")

# Task 9: Merge JSON files
print("\n9. Merging JSON files:")
data1 = {'a': 1, 'b': 2}
data2 = {'c': 3, 'd': 4}
with open('file1.json', 'w') as f:
    json.dump(data1, f)
with open('file2.json', 'w') as f:
    json.dump(data2, f)
with open('file1.json', 'r') as f:
    merged = json.load(f)
with open('file2.json', 'r') as f:
    merged.update(json.load(f))
print(f"   Merged: {merged}")

# Task 10: Validate JSON structure
print("\n10. Validating JSON structure:")
required_keys = ['name', 'age']
test_data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
has_all_keys = all(key in test_data for key in required_keys)
print(f"   Has all required keys: {has_all_keys}")

# Cleanup
for file in [json_file, 'pretty.json', 'nested.json', 'file1.json', 'file2.json']:
    if os.path.exists(file):
        os.remove(file)

print("\n✅ Solution completed!")
