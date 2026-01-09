#!/usr/bin/env python3
"""
Example 1: File Reading/Writing
Demonstrate basic file operations
"""

# Writing to a file
with open('example.txt', 'w') as f:
    f.write("Hello, Python!\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print("File written successfully!")

# Reading entire file
print("\n=== Reading entire file ===")
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
print("\n=== Reading line by line ===")
with open('example.txt', 'r') as f:
    for line in f:
        print(f"Line: {line.strip()}")

# Reading all lines into list
print("\n=== Reading all lines ===")
with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")
