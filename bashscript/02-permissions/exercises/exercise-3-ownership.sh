#!/bin/bash
# Exercise 3: File Ownership
# Complete the tasks below by adding the appropriate commands
# Note: Some commands may require sudo

# Create test files
mkdir -p ownership_exercise
cd ownership_exercise
touch file1.txt file2.txt
mkdir testdir

# Task 1: Display current owner and group of file1.txt
# Add command here:


# Task 2: Display owner and group of all files
# Add command here:


# Task 3: Change owner of file1.txt (if you have permission)
# Hint: sudo chown newowner file1.txt
# Add command here (commented out if not needed):


# Task 4: Change group of file2.txt
# Hint: chgrp newgroup file2.txt or chown :newgroup file2.txt
# Add command here (commented out if not needed):


# Task 5: Change both owner and group of testdir
# Add command here (commented out if not needed):


# Task 6: Change ownership recursively for all files in current directory
# Add command here (commented out if not needed):


# Task 7: Display your current username
# Add command here:


# Task 8: Display your current group
# Add command here:


# Task 9: Show all groups you belong to
# Add command here:


# Task 10: Verify ownership changes
echo "Current ownership:"
# Add command here:


cd ..
rm -rf ownership_exercise
echo "Exercise 3 completed! Check your work above."
