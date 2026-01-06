#!/bin/bash
# Exercise 5: umask Practice
# Complete the tasks below by adding the appropriate commands

# Task 1: Display current umask value
# Add command here:


# Task 2: Display current umask in symbolic notation
# Hint: umask -S
# Add command here:


# Task 3: Set umask to 022 (common default)
# Add command here:


# Task 4: Create a file and check its permissions
touch umask_test.txt
# Add command to check permissions:


# Task 5: Create a directory and check its permissions
mkdir umask_test_dir
# Add command to check permissions:


# Task 6: Set umask to 077 (very restrictive)
# Add command here:


# Task 7: Create files and directories with new umask
touch secure_file.txt
mkdir secure_dir
# Add command to check permissions:


# Task 8: Calculate what permissions a file will have with umask 022
# Default file permissions: 666, umask: 022, result: ?
# Add your calculation here (as a comment):


# Task 9: Calculate what permissions a directory will have with umask 022
# Default directory permissions: 777, umask: 022, result: ?
# Add your calculation here (as a comment):


# Task 10: Restore umask to original value (you may need to note it first)
# Add command here:


# Cleanup
rm -rf umask_test.txt umask_test_dir secure_file.txt secure_dir
echo "Exercise 5 completed! Check your work above."
