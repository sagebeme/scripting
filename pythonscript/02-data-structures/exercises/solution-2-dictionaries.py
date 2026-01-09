#!/usr/bin/env python3
"""
Solution: Exercise 2 - Dictionaries
Complete solution for dictionary operations
"""

# Task 1: Create a dictionary with name, age, city
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Person: {person}")

# Task 2: Access dictionary values
name = person['name']
print(f"Name: {name}")

# Task 3: Add a new key-value pair
person['email'] = 'alice@example.com'
print(f"After adding email: {person}")

# Task 4: Use dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 5)}
print(f"Squares dict: {squares_dict}")

# Task 5: Merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# Task 6: Get dictionary keys and values as lists
data = {'name': 'Bob', 'age': 25, 'city': 'London'}
keys = list(data.keys())
values = list(data.values())
print(f"Keys: {keys}")
print(f"Values: {values}")

# Task 7: Create nested dictionary
nested = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}
print(f"Nested: {nested}")

# Task 8: Access nested dictionary values
nested_data = {'person': {'name': 'Alice', 'details': {'age': 30, 'city': 'NYC'}}}
city = nested_data['person']['details']['city']
print(f"City: {city}")

# Task 9: Filter dictionary by value
data = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
filtered = {k: v for k, v in data.items() if v > 10}
print(f"Filtered (value > 10): {filtered}")

# Task 10: Invert dictionary (swap keys and values)
original = {1: 'a', 2: 'b', 3: 'c'}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

print("\n✅ Exercise 2 completed!")
