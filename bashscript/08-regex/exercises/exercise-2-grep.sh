#!/bin/bash
# Exercise 2: grep Usage
# Complete the tasks below by adding the appropriate commands

# Create test files
mkdir -p grep_test
cd grep_test
cat > file1.txt << EOF
Error: connection failed
Warning: low memory
Info: process started
Error: timeout occurred
EOF

cat > file2.txt << EOF
Success: operation completed
Error: invalid input
Info: system ready
EOF

# Task 1: Search for "Error" in file1.txt
# Add command here:


# Task 2: Search case-insensitively for "error"
# Use -i option
# Add command here:


# Task 3: Invert match - show lines NOT containing "Error"
# Use -v option
# Add command here:


# Task 4: Show line numbers with matches
# Use -n option
# Add command here:


# Task 5: Show only filenames with matches
# Use -l option
# Add command here:


# Task 6: Search recursively in directory
# Use -r option
# Add command here:


# Task 7: Use extended regex to match "Error" or "Warning"
# Use -E option with pattern Error|Warning
# Add command here:


# Task 8: Count matches
# Use -c option
# Add command here:


# Task 9: Match whole words only
# Use -w option
# Add command here:


# Task 10: Show context lines (before and after match)
# Use -A and -B options
# Add command here:


cd ..
rm -rf grep_test
echo "Exercise 2 completed! Check your work above."
