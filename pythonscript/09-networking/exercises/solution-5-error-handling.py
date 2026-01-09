#!/usr/bin/env python3
"""
Solution: Exercise 5 - Error Handling
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 5 - Error Handling")
print("=" * 60)

# Solution implementation
# This demonstrates one approach to solving the exercise
# Refer to the exercise file for specific requirements


try:
    result = 10 / 2
    print(f"1. Result: {result}")
except ZeroDivisionError:
    print("1. Division by zero")
except Exception as e:
    print(f"1. Error: {e}")
else:
    print("1. No errors occurred")
finally:
    print("1. Finally block executed")

print("\n✅ Solution completed!")
