#!/bin/bash
# Exercise 2: Pipes and Filters
# Complete the tasks below by adding the appropriate commands

# Create test files
mkdir -p pipe_exercise
cd pipe_exercise
cat > data.txt << EOF
apple
banana
apple
cherry
banana
date
apple
EOF

# Task 1: Count lines in data.txt using wc
# Add command here:


# Task 2: Search for "apple" in data.txt using grep
# Add command here:


# Task 3: Sort data.txt and display
# Add command here:


# Task 4: Sort and remove duplicates (unique lines)
# Add command here:


# Task 5: Count how many times "apple" appears
# Hint: Use grep and wc
# Add command here:


# Task 6: Get first 3 lines of sorted data
# Add command here:


# Task 7: Get last 2 lines of data
# Add command here:


# Task 8: Chain multiple commands: sort, unique, count lines
# Add command here:


# Task 9: Find lines containing "a" and count them
# Add command here:


# Task 10: Extract first column from /etc/passwd (if available)
# Hint: cut -d: -f1
# Add command here (commented if /etc/passwd not accessible):


cd ..
rm -rf pipe_exercise
echo "Exercise 2 completed! Check your work above."
