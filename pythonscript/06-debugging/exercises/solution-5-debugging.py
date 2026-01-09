#!/usr/bin/env python3
"""
Solution: Exercise 5 - Debugging
"""
import pdb

print("=" * 60)
print("Solution: Exercise 5 - Debugging")
print("=" * 60)

def divide(a, b):
    # pdb.set_trace()  # Uncomment to debug
    return a / b

result = divide(10, 2)
print(f"1. Result: {result}")

# Using assert for debugging
assert result == 5, "Division failed"
print("2. Assert passed")

# Using print for debugging
x = 10
y = 20
print(f"3. Debug values: x={x}, y={y}")

print("\n✅ Solution completed!")
