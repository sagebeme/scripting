#!/usr/bin/env python3
"""
Example 4: Function Examples
Demonstrate function definition and usage
"""

# Simple function
def greet():
    print("Hello from function!")

print("1. Simple function:")
greet()

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

print("\n2. Function with parameter:")
greet_user("Python Learner")

# Function with return value
def get_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

print("\n3. Function returning value:")
current_date = get_date()
print(f"Today is: {current_date}")

# Function with multiple parameters
def add(a, b):
    return a + b

print("\n4. Function with multiple parameters:")
result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with default parameters
def display_info(name="Guest", age=0):
    print(f"Name: {name}, Age: {age}")

print("\n5. Function with default parameters:")
display_info()
display_info("John", 25)

# Lambda function
square = lambda x: x ** 2
print("\n6. Lambda function:")
print(f"Square of 5: {square(5)}")
