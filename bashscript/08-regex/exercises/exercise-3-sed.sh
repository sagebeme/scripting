#!/bin/bash
# Exercise 3: sed Basics
# Complete the tasks below by adding the appropriate commands

# Create test file
cat > test.txt << EOF
hello world
test123
abc123def
replace me
multiple replace replace
EOF

# Task 1: Replace first occurrence of 'replace' with 'changed'
# Use sed substitution
# Add command here (display result):


# Task 2: Replace all occurrences of 'replace' with 'changed'
# Use g flag
# Add command here (display result):


# Task 3: Replace and save to new file
# Add command here:


# Task 4: Delete lines containing 'test'
# Use d command
# Add command here (display result):


# Task 5: Print only lines matching pattern
# Use -n and p
# Add command here:


# Task 6: Replace on specific line number
# Replace on line 2 only
# Add command here (display result):


# Task 7: Replace with case-insensitive match
# Use I flag (GNU sed) or pattern
# Add command here (display result):


# Task 8: Multiple substitutions
# Replace 'hello' and 'world' in one command
# Add command here (display result):


# Task 9: Use sed script file
# Create script.sed and use it
# Add commands here:


# Task 10: In-place editing (GNU sed)
# Use -i option to edit file
# Add command here:


# Cleanup
rm -f test.txt newfile.txt script.sed
echo "Exercise 3 completed! Check your work above."
