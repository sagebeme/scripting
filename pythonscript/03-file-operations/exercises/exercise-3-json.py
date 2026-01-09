#!/usr/bin/env python3
"""
Exercise 3: JSON Operations
Complete the tasks below by adding the appropriate code
"""

import json

# Task 1: Write dictionary to JSON file
# Create a dictionary and write it to 'data.json'
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
# Add your code here:


# Task 2: Read JSON file
# Read 'data.json' and print the data
# Add your code here:


# Task 3: Pretty print JSON
# Write JSON with indentation for readability
# Add your code here:


# Task 4: Read JSON string
# Parse a JSON string into Python object
json_string = '{"name": "Bob", "age": 25}'
# Add your code here:


# Task 5: Convert Python object to JSON string
# Convert a dictionary to JSON string
person = {'name': 'Charlie', 'age': 35}
# Add your code here:


# Task 6: Handle JSON errors
# Try to parse invalid JSON and handle error
invalid_json = "{'name': 'Invalid'}"  # Invalid JSON (uses single quotes)
# Add your code here:


# Task 7: Read nested JSON
# Read JSON with nested structures
nested_data = {
    'person': {
        'name': 'David',
        'details': {
            'age': 40,
            'city': 'Boston'
        }
    }
}
# Write and read this nested JSON
# Add your code here:


# Task 8: Update JSON file
# Read JSON, modify it, and write back
# Add your code here:


# Task 9: Merge JSON files
# Read two JSON files and merge them
# Add your code here:


# Task 10: Validate JSON structure
# Check if JSON has required keys
required_keys = ['name', 'age']
# Add your code here:


print("Exercise 3 completed! Check your work above.")
