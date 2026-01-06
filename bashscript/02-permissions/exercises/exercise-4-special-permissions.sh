#!/bin/bash
# Exercise 4: Special Permissions
# Complete the tasks below by adding the appropriate commands
# Note: Some commands may require sudo

# Create test files
mkdir -p special_exercise
cd special_exercise
touch testfile.sh
mkdir sharedir

# Task 1: Set SUID bit on testfile.sh (if you have permission)
# Hint: chmod u+s or chmod 4755
# Add command here (commented out if not needed):


# Task 2: Set SGID bit on sharedir
# Hint: chmod g+s or chmod 2755
# Add command here:


# Task 3: Set sticky bit on sharedir
# Hint: chmod +t or chmod 1755
# Add command here:


# Task 4: Display permissions to see special bits (s, S, t, T)
# Add command here:


# Task 5: Remove SUID bit from testfile.sh
# Add command here:


# Task 6: Set both SUID and execute for owner (4755)
# Add command here:


# Task 7: Set SGID on directory with execute for group (2755)
# Add command here:


# Task 8: Explain what each special permission does (add comments)
# SUID:
# Add comment here:


# SGID:
# Add comment here:


# Sticky bit:
# Add comment here:


cd ..
rm -rf special_exercise
echo "Exercise 4 completed! Check your work above."
