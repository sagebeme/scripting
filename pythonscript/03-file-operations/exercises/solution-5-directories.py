#!/usr/bin/env python3
"""
Solution: Exercise 5 - Directory Operations
Complete solution for the exercise
"""

import os
from pathlib import Path
import shutil

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 5 - Directory Operations")
print("=" * 60)

# Task 1: List directory contents
print("1. Directory contents:")
for item in os.listdir('.'):
    print(f"   {item}")

# Task 2: Walk directory tree
print("\n2. Walking directory tree (first 5 items):")
count = 0
for root, dirs, files in os.walk('.'):
    if count >= 5:
        break
    print(f"   {root}: {len(files)} files")
    count += 1

# Task 3: Create nested directories
print("\n3. Creating nested directories:")
nested_path = Path('parent/child/grandchild')
nested_path.mkdir(parents=True, exist_ok=True)
print(f"   Created: {nested_path}")

# Task 4: Get file size
test_file = Path('size_test.txt')
test_file.write_text('This is a test file for size calculation.')
file_size = test_file.stat().st_size
print(f"4. File size: {file_size} bytes")

# Task 5: Check if path is file or directory
print("\n5. Checking path types:")
print(f"   {test_file} is file: {test_file.is_file()}")
print(f"   {nested_path} is directory: {nested_path.is_dir()}")

# Task 6: Get absolute path
relative_path = Path('size_test.txt')
absolute_path = relative_path.resolve()
print(f"6. Absolute path: {absolute_path}")

# Task 7: Find files by extension
print("\n7. Finding .txt files:")
txt_files = list(Path('.').glob('*.txt'))
for txt_file in txt_files[:5]:  # Show first 5
    print(f"   {txt_file}")

# Task 8: Remove directory
print("\n8. Removing directory:")
if nested_path.exists():
    nested_path.rmdir()  # Remove grandchild
    nested_path.parent.rmdir()  # Remove child
    nested_path.parent.parent.rmdir()  # Remove parent
print("   Directories removed")

# Task 9: Copy directory structure
print("\n9. Copying directory structure:")
source = Path('source_dir')
source.mkdir(exist_ok=True)
(source / 'subdir').mkdir(exist_ok=True)
dest = Path('dest_dir')
if dest.exists():
    shutil.rmtree(dest)
shutil.copytree(source, dest, dirs_exist_ok=True)
print(f"   Copied {source} to {dest}")

# Task 10: Get directory size
print("\n10. Calculating directory size:")
total_size = 0
for file_path in Path('.').rglob('*.txt'):
    if file_path.is_file():
        total_size += file_path.stat().st_size
print(f"   Total size of .txt files: {total_size} bytes")

# Cleanup
if test_file.exists():
    test_file.unlink()
if source.exists():
    shutil.rmtree(source)
if dest.exists():
    shutil.rmtree(dest)

print("\n✅ Solution completed!")
