#!/bin/bash
# Exercise 5: Input Validation
# Complete the tasks below by adding the appropriate commands

# Task 1: Create a function 'validate_count' that checks if exactly 2 arguments were provided
# If not, display error and return 1
# Add function definition here:


# Task 2: Create a function 'validate_file' that checks if a file exists
# Take filename as parameter
# Return 0 if exists, 1 if not, display error
# Add function definition here:


# Task 3: Create a function 'validate_number' that checks if argument is a number
# Use pattern matching or arithmetic check
# Add function definition here:


# Task 4: Create a function 'validate_directory' that checks if path is a directory
# Add function definition here:


# Task 5: Test validate_count with different argument counts
# Test with 0, 1, 2, 3 arguments
# Add test calls here:


# Task 6: Test validate_file
# Create a test file, then validate it
touch testfile.txt
# Add test calls here:


# Task 7: Test validate_number
# Test with number, string, empty
# Add test calls here:


# Task 8: Test validate_directory
# Test with existing directory, non-existent path
mkdir -p testdir
# Add test calls here:


# Task 9: Create a comprehensive validation function
# Function 'validate_input' should validate:
# - Argument count
# - File existence
# - Directory existence
# Add function definition here:


# Task 10: Use validate_input in a script scenario
# Add usage example here:


# Cleanup
rm -f testfile.txt
rm -rf testdir
echo "Exercise 5 completed! Check your work above."
