#!/usr/bin/env python3
"""
Solution: Exercise 1 - Basic Patterns
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 1 - Basic Patterns")
print("=" * 60)

# Solution implementation
# This demonstrates one approach to solving the exercise
# Refer to the exercise file for specific requirements


import re

text = "Hello 123 World"
print(f"1. Digits: {re.findall(r'\\d+', text)}")
print(f"2. Words: {re.findall(r'\\w+', text)}")
print(f"3. Match: {re.search(r'\\d+', text).group()}")

print("\n✅ Solution completed!")
