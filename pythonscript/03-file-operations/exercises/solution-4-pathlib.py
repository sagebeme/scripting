#!/usr/bin/env python3
"""
Solution: Exercise 4 - Path Operations with pathlib
Complete solution for the exercise
"""

from pathlib import Path
import os

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 4 - Path Operations with pathlib")
print("=" * 60)

# Task 1: Create Path object
current_dir = Path('.')
print(f"1. Current directory Path: {current_dir}")

# Task 2: Check if path exists
test_file = Path('test_file.txt')
test_file.write_text('test content')
exists = test_file.exists()
print(f"2. Path exists: {exists}")

# Task 3: Get current working directory
cwd = Path.cwd()
print(f"3. Current working directory: {cwd}")

# Task 4: Join paths
directory = Path('data')
filename = 'file.txt'
full_path = directory / filename
print(f"4. Joined path: {full_path}")

# Task 5: Get file extension
file_path = Path('document.txt')
extension = file_path.suffix
print(f"5. File extension: {extension}")

# Task 6: Get file name without extension
name_without_ext = file_path.stem
print(f"6. Name without extension: {name_without_ext}")

# Task 7: List directory contents
print("\n7. Directory contents:")
for item in Path('.').iterdir():
    if item.is_file() and item.name.startswith('test'):
        print(f"   {item.name}")

# Task 8: Create directory
new_dir = Path('test_directory')
new_dir.mkdir(exist_ok=True)
print(f"8. Directory created: {new_dir.exists()}")

# Task 9: Read text file
content = test_file.read_text()
print(f"9. File content: {content}")

# Task 10: Write text file
write_file = Path('output.txt')
write_file.write_text('Hello, pathlib!')
print(f"10. File written: {write_file.read_text()}")

# Cleanup
if test_file.exists():
    test_file.unlink()
if write_file.exists():
    write_file.unlink()
if new_dir.exists():
    new_dir.rmdir()

print("\n✅ Solution completed!")
