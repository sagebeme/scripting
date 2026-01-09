#!/usr/bin/env python3
"""
Solution: Exercise 3 - Sets and Tuples
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 3 - Sets and Tuples")
print("=" * 60)

# Task 1: Create a set with numbers
numbers_set = {1, 2, 3, 4, 5}
print(f"1. Set: {numbers_set}")

# Task 2: Add and remove items from set
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(2)
print(f"2. After add(4) and remove(2): {numbers}")

# Task 3: Set operations (union, intersection, difference)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
print(f"3. Union: {union}")
print(f"   Intersection: {intersection}")
print(f"   Difference: {difference}")

# Task 4: Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"4. Tuple: {my_tuple}")

# Task 5: Tuple unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"5. Unpacked: x={x}, y={y}")

# Task 6: Named tuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(f"6. Named tuple: {point}, x={point.x}, y={point.y}")

# Task 7: Use set to remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
unique = list(set(numbers))
print(f"7. Unique (unordered): {unique}")

# Task 8: Check if sets are subsets
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(f"8. {set1} is subset of {set2}: {is_subset}")

# Task 9: Create set comprehension
squares_set = {x**2 for x in range(1, 11)}
print(f"9. Set of squares: {squares_set}")

# Task 10: Multiple assignment with tuples
a = 10
b = 20
a, b = b, a  # Swap using tuple unpacking
print(f"10. After swap: a={a}, b={b}")

print("\n✅ Solution completed!")
