#!/usr/bin/env python3
"""
Solution: Exercise 1 - Lists
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 1 - Lists")
print("=" * 60)

# List operations and comprehensions
numbers = list(range(1, 11))
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Evens: {evens}")

print("\n✅ Solution completed!")
