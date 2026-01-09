#!/usr/bin/env python3
"""
Solution: Exercise 5 - System Info
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 5 - System Info")
print("=" * 60)

# Solution implementation
# This demonstrates one approach to solving the exercise
# Refer to the exercise file for specific requirements


import os

print(f"1. CWD: {os.getcwd()}")
print(f"2. Files: {len(os.listdir('.'))} items")
print(f"3. Path exists: {os.path.exists('README.md')}")
print(f"4. HOME: {os.environ.get('HOME', 'N/A')}")

print("\n✅ Solution completed!")
