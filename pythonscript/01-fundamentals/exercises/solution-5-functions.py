#!/usr/bin/env python3
"""
Solution: Exercise 5 - Functions
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 5 - Functions")
print("=" * 60)

# Task 1: Define a simple function that prints "Hello"
def greet():
    print("Hello")

# Task 2: Call the function
print("1-2. Simple function:")
greet()

# Task 3: Define a function that takes a parameter
def greet_user(name):
    print(f"Hello, {name}!")

# Task 4: Call the function with your name
print("\n3-4. Function with parameter:")
greet_user("Python Learner")

# Task 5: Define a function that returns a value
def square(number):
    return number ** 2

# Task 6: Call the function and print the result
print("\n5-6. Function returning value:")
result = square(5)
print(f"Square of 5: {result}")

# Task 7: Define a function with default parameter
def greet_with_default(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Task 8: Call function with and without default
print("\n7-8. Function with default parameter:")
greet_with_default("Bob")  # Uses default
greet_with_default("Charlie", "Hi")  # Overrides default

# Task 9: Define a function with multiple parameters
def add(a, b):
    return a + b

# Task 10: Call function with multiple arguments
print("\n9-10. Function with multiple parameters:")
result = add(5, 3)
print(f"5 + 3 = {result}")

print("\n✅ Solution completed!")
