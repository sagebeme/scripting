#!/usr/bin/env python3
"""
Example 2: Dictionary Operations
Show dictionary manipulation techniques
"""

print("=== Dictionary Operations ===")
print()

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}
print(f"1. Squares dict: {squares_dict}")
print()

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"2. Even squares: {even_squares}")
print()

# Invert dictionary
original = {1: 'a', 2: 'b', 3: 'c'}
inverted = {v: k for k, v in original.items()}
print(f"3. Inverted: {inverted}")
print()

# Merge dictionaries (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(f"4. Merged: {merged}")
print()

# Nested dictionary
nested = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}
print(f"5. Nested dict: {nested}")
print(f"   Person1 name: {nested['person1']['name']}")
print()

# Dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'NYC']
person = dict(zip(keys, values))
print(f"6. From lists: {person}")
