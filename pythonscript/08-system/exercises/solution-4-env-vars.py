#!/usr/bin/env python3
"""
Solution: Exercise 4 - Environment Variables
"""
import os

print("=" * 60)
print("Solution: Exercise 4 - Environment Variables")
print("=" * 60)

print(f"1. HOME: {os.environ.get('HOME', 'N/A')}")
print(f"2. PATH: {os.environ.get('PATH', 'N/A')[:50]}...")
print(f"3. USER: {os.environ.get('USER', 'N/A')}")

os.environ['MY_VAR'] = 'test_value'
print(f"4. MY_VAR: {os.environ.get('MY_VAR')}")

print("\n✅ Solution completed!")
