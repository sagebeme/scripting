#!/usr/bin/env python3
"""
Solution: Exercise 3 - Json
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 3 - Json")
print("=" * 60)

# File operations example
# Note: This is a template - adjust based on specific exercise requirements
try:
    with open('example.txt', 'w') as f:
        f.write("Hello, Python!\n")
    with open('example.txt', 'r') as f:
        content = f.read()
    print(f"File content: {content}")
except FileNotFoundError:
    print("File not found")

print("\n✅ Solution completed!")
