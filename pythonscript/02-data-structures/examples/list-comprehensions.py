#!/usr/bin/env python3
"""
Example 1: List Comprehensions
Demonstrate powerful list operations
"""

print("=== List Comprehensions ===")
print()

# Basic list comprehension
squares = [x**2 for x in range(10)]
print(f"1. Squares: {squares}")
print()

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"2. Even numbers: {evens}")
print()

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"3. Matrix: {matrix}")
print()

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"4. Flattened: {flattened}")
print()

# Multiple conditions
filtered = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(f"5. Divisible by 2 and 3: {filtered}")
print()

# With else clause
result = [x if x % 2 == 0 else -x for x in range(10)]
print(f"6. With else: {result}")
