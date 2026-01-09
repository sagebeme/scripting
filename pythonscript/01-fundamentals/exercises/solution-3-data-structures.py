#!/usr/bin/env python3
"""
Solution: Exercise 3 - Data Structures
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 3 - Data Structures")
print("=" * 60)

# Task 1: Create a list with three items
my_list = ['apple', 'banana', 'cherry']
print(f"1. List: {my_list}")

# Task 2: Add an item to the list
my_list.append('orange')
print(f"2. After append: {my_list}")

# Task 3: Remove an item from the list
my_list.remove('banana')
print(f"3. After remove: {my_list}")

# Task 4: Get the length of the list
length = len(my_list)
print(f"4. Length: {length}")

# Task 5: Access list elements
first_item = my_list[0]
last_item = my_list[-1]
print(f"5. First: {first_item}, Last: {last_item}")

# Task 6: Create a dictionary with key-value pairs
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"6. Dictionary: {person}")

# Task 7: Access dictionary values
name = person['name']
print(f"7. Name: {name}")

# Task 8: Add a new key-value pair to dictionary
person['email'] = 'alice@example.com'
print(f"8. After adding email: {person}")

# Task 9: Iterate through a list
print("9. Iterating through list:")
for item in my_list:
    print(f"   - {item}")

# Task 10: Iterate through a dictionary
print("10. Iterating through dictionary:")
for key, value in person.items():
    print(f"    {key}: {value}")

print("\n✅ Solution completed!")
