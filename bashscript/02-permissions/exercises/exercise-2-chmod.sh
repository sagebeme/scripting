#!/bin/bash
# Exercise 2: Changing Permissions with chmod
# Complete the tasks below by adding the appropriate commands

# Create test files
mkdir -p chmod_exercise
cd chmod_exercise
touch file1.txt file2.txt script.sh
mkdir mydir

# Task 1: Make file1.txt readable and writable by owner only (600)
# Add command here:


# Task 2: Add execute permission for owner on script.sh using symbolic notation
# Add command here:


# Task 3: Remove write permission for group and others on file2.txt
# Add command here:


# Task 4: Set permissions to 755 (rwxr-xr-x) on script.sh using octal notation
# Add command here:


# Task 5: Make mydir accessible only by owner (700)
# Add command here:


# Task 6: Add read permission for group on file1.txt using symbolic notation
# Add command here:


# Task 7: Set file2.txt to rw-r--r-- (644) using octal
# Add command here:


# Task 8: Make script.sh executable for all users using symbolic notation
# Add command here:


# Task 9: Verify permissions were set correctly
echo "Current permissions:"
# Add command here:


cd ..
rm -rf chmod_exercise
echo "Exercise 2 completed! Check your work above."
