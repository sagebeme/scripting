#!/usr/bin/env python3
"""
Solution: Exercise 2 - Regex Groups
"""
import re

print("=" * 60)
print("Solution: Exercise 2 - Regex Groups")
print("=" * 60)

text = "Contact: john@example.com or jane@test.com"
pattern = r'(\w+)@(\w+\.\w+)'
matches = re.findall(pattern, text)
print(f"1. Matches: {matches}")

match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    print(f"2. Full match: {match.group(0)}")
    print(f"3. Group 1 (username): {match.group(1)}")
    print(f"4. Group 2 (domain): {match.group(2)}")

pattern = r'(?P<name>\w+)@(?P<domain>\w+\.\w+)'
match = re.search(pattern, text)
if match:
    print(f"5. Named groups: {match.groupdict()}")

print("\n✅ Solution completed!")
