#!/usr/bin/env python3
"""
Solution: Exercise 1 - Basic File I/O
Complete solution for file operations
"""

# Task 1: Write text to a file
with open('test.txt', 'w') as f:
    f.write("Hello, Python!\n")
print("✓ File written")

# Task 2: Read text from a file
with open('test.txt', 'r') as f:
    content = f.read()
print(f"✓ File content: {content}")

# Task 3: Use context manager (with statement)
with open('test2.txt', 'w') as f:
    f.write("Using context manager\n")
print("✓ Context manager used")

# Task 4: Append to a file
with open('test.txt', 'a') as f:
    f.write("New line\n")
print("✓ Appended to file")

# Task 5: Read file line by line
print("\nReading line by line:")
with open('test.txt', 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"  Line {line_num}: {line.strip()}")

# Task 6: Handle file errors
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("\n✓ Handled FileNotFoundError: File does not exist")

# Task 7: Write multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
with open('multiline.txt', 'w') as f:
    for line in lines:
        f.write(line + '\n')
print("✓ Multiple lines written")

# Task 8: Read all lines into a list
with open('multiline.txt', 'r') as f:
    all_lines = f.readlines()
print(f"✓ All lines: {[line.strip() for line in all_lines]}")

# Task 9: Check if file exists
import os
if os.path.exists('test.txt'):
    print("✓ File exists")
else:
    print("✗ File does not exist")

# Task 10: Copy file content
with open('test.txt', 'r') as source:
    content = source.read()
with open('copy.txt', 'w') as dest:
    dest.write(content)
print("✓ File copied")

# Cleanup
import os
for file in ['test.txt', 'test2.txt', 'multiline.txt', 'copy.txt']:
    if os.path.exists(file):
        os.remove(file)
        print(f"✓ Cleaned up {file}")

print("\n✅ Exercise 1 completed!")
