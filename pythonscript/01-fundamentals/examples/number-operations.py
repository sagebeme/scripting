#!/usr/bin/env python3
"""
Example 2: Number Operations
Demonstrate arithmetic operations and formatting
"""

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
print(f"\nResults:")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")

# Handle division by zero
if num2 != 0:
    print(f"Quotient: {num1 / num2}")
    print(f"Floor Division: {num1 // num2}")
    print(f"Modulo: {num1 % num2}")
else:
    print("Cannot divide by zero")

# Power operation
print(f"Power ({num1} to the power of {num2}): {num1 ** num2}")
