#!/usr/bin/env python3
"""
Solution: Exercise 4 - Control Flow
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 4 - Control Flow")
print("=" * 60)

# Task 1: Write an if statement
num = 5
if num > 0:
    print(f"1. {num} is positive")

# Task 2: Write if/else statement
if num % 2 == 0:
    print(f"2. {num} is even")
else:
    print(f"2. {num} is odd")

# Task 3: Write if/elif/else statement
number = -5
if number > 0:
    print(f"3. {number} is positive")
elif number < 0:
    print(f"3. {number} is negative")
else:
    print(f"3. {number} is zero")

# Task 4: Create a for loop
print("4. For loop 1 to 5:")
for i in range(1, 6):
    print(f"   {i}")

# Task 5: Create a while loop
print("5. While loop 1 to 5:")
count = 1
while count <= 5:
    print(f"   {count}")
    count += 1

# Task 6: Use break in a loop
print("6. Loop with break at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(f"   {i}")

# Task 7: Use continue in a loop
print("7. Loop with continue (skip evens):")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"   {i}")

# Task 8: Nested loops
print("8. Nested loops (multiplication table 1x1 to 3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"   {i} x {j} = {i * j}")

# Task 9: Loop through a list
print("9. Loop through list:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"   {fruit}")

# Task 10: Conditional with logical operators
number = 15
if 10 <= number <= 20:
    print(f"10. {number} is between 10 and 20")

print("\n✅ Solution completed!")
