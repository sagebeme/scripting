#!/usr/bin/env python3
"""
Example 3: List Operations
Demonstrate list manipulation and methods
"""

# Create a list
numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# Add elements
numbers.append(6)
print(f"After append(6): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

# Remove elements
numbers.remove(3)
print(f"After remove(3): {numbers}")

# List methods
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")

# List slicing
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle: {numbers[2:5]}")

# List comprehension
squared = [x**2 for x in numbers]
print(f"Squared: {squared}")

# Iterate through list
print("\nIterating through list:")
for num in numbers:
    print(f"  {num}")
