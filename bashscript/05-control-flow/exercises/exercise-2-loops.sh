#!/bin/bash
# Exercise 2: Loops
# Complete the tasks below by adding the appropriate commands

# Task 1: For loop - iterate over a list
items="apple banana cherry"
# Loop through items and display each
# Add for loop here:


# Task 2: For loop - iterate over files
# Create test files first
touch file1.txt file2.txt file3.txt
# Loop through .txt files and display names
# Add for loop here:


# Task 3: C-style for loop
# Count from 1 to 5
# Add for loop here:


# Task 4: While loop - count down from 5 to 1
count=5
# Add while loop here:


# Task 5: While loop - read file line by line
# Create test file
echo -e "line1\nline2\nline3" > testfile.txt
# Read and display each line
# Add while loop here:


# Task 6: Until loop - wait until file exists
# Create file after 2 seconds in background
(sleep 2 && touch waitfile.txt) &
# Wait until file exists
# Add until loop here:


# Task 7: Nested loops
# Create a multiplication table (1-3)
# Add nested loops here:


# Task 8: Loop with break
# Loop from 1 to 10, break at 5
# Add loop with break here:


# Task 9: Loop with continue
# Loop from 1 to 10, skip even numbers
# Add loop with continue here:


# Cleanup
rm -f file*.txt testfile.txt waitfile.txt
echo "Exercise 2 completed! Check your work above."
