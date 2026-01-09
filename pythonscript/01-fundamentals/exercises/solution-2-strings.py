#!/usr/bin/env python3
"""
Solution: Exercise 2 - Strings
Complete solution for the exercise
"""

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 2 - Strings")
print("=" * 60)

# Task 1: Create a string variable with your name
my_name = "Python Learner"
print(f"1. Name: {my_name}")

# Task 2: Convert the string to uppercase
upper_name = my_name.upper()
print(f"2. Uppercase: {upper_name}")

# Task 3: Convert the string to lowercase
lower_name = my_name.lower()
print(f"3. Lowercase: {lower_name}")

# Task 4: Get the length of the string
length = len(my_name)
print(f"4. Length: {length}")

# Task 5: Replace a character in the string
text = "python"
replaced = text.replace('a', 'A')  # No 'a' in "python"
replaced2 = text.replace('p', 'P')
print(f"5. Replaced 'p' with 'P': {replaced2}")

# Task 6: Split a string into a list
text_to_split = "hello world python"
words = text_to_split.split()
print(f"6. Split: {words}")

# Task 7: Join a list into a string
word_list = ['Python', 'is', 'great']
joined = ' '.join(word_list)
print(f"7. Joined: {joined}")

# Task 8: Slice a string
full_text = "Python Programming"
first_five = full_text[:5]
print(f"8. First 5 characters: {first_five}")

# Task 9: Use f-string formatting
name = "Alice"
age = 30
message = f"My name is {name} and I'm {age} years old"
print(f"9. F-string: {message}")

# Task 10: Check if a substring exists
text = "I love Python programming"
contains = "python" in text.lower()
print(f"10. Contains 'python': {contains}")

print("\n✅ Solution completed!")
