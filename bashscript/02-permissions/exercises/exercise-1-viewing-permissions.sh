#!/bin/bash
# Exercise 1: Viewing Permissions
# Complete the tasks below by adding the appropriate commands

# Create a test directory for this exercise
mkdir -p perm_exercise
cd perm_exercise

# Create some test files
touch file1.txt file2.txt script.sh
mkdir testdir

# Task 1: List files with detailed permissions (long format)
# Add command here:


# Task 2: List files showing numeric permissions (octal)
# Hint: Use ls -l and stat
# Add command here:


# Task 3: Display permissions of a specific file (file1.txt)
# Add command here:


# Task 4: Show only the permission string (e.g., -rw-r--r--)
# Hint: Use ls -l and cut or awk
# Add command here:


# Task 5: Count files with execute permission
# Add command here:


# Task 6: List only directories with their permissions
# Add command here:


# Task 7: Display file type and permissions together
# Add command here:


# Task 8: Show permissions in human-readable format
# Add command here:


cd ..
rm -rf perm_exercise
echo "Exercise 1 completed! Check your work above."
