#!/bin/bash
# Exercise 1: Conditional Statements
# Complete the tasks below by adding the appropriate commands

# Task 1: Check if a file exists and display message
file="test.txt"
touch "$file"
# Add if statement here:


# Task 2: Check if a directory exists, create if it doesn't
dir="testdir"
# Add if statement here:


# Task 3: Compare two numbers
a=10
b=5
# Check if a is greater than b
# Add if statement here:


# Task 4: Check if a string is empty
str=""
# Add if statement to check if empty:


# Task 5: If/else statement
# Check if user is root, display appropriate message
# Add if/else statement here:


# Task 6: If/elif/else statement
# Check file type (regular file, directory, or other)
check_file="test.txt"
# Add if/elif/else statement here:


# Task 7: Nested conditionals
# Check if file exists AND is readable
# Add nested if statement here:


# Task 8: Multiple conditions with && and ||
# Check if file exists OR create it
# Add statement here:


# Cleanup
rm -f test.txt
rm -rf testdir
echo "Exercise 1 completed! Check your work above."
