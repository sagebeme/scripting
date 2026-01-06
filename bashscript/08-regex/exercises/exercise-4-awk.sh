#!/bin/bash
# Exercise 4: awk Basics
# Complete the tasks below by adding the appropriate commands

# Create test file
cat > data.txt << EOF
John 25 Engineer
Jane 30 Doctor
Bob 28 Teacher
Alice 32 Lawyer
EOF

# Task 1: Print first field (name) of each line
# Add command here:


# Task 2: Print first and third fields
# Add command here:


# Task 3: Print lines where age > 28
# Use pattern matching
# Add command here:


# Task 4: Calculate sum of ages (second field)
# Add command here:


# Task 5: Print formatted output
# Format: "Name: [name], Age: [age]"
# Add command here:


# Task 6: Count lines
# Add command here:


# Task 7: Print lines matching pattern
# Lines containing "Engineer"
# Add command here:


# Task 8: Use custom field separator
# Create file with : separator and process
echo "name:age:job" > custom.txt
echo "John:25:Engineer" >> custom.txt
# Process with : as separator
# Add command here:


# Task 9: Calculate average age
# Add command here:


# Task 10: Print with conditions
# Print "Senior" if age > 30, else "Junior"
# Add command here:


# Cleanup
rm -f data.txt custom.txt
echo "Exercise 4 completed! Check your work above."
