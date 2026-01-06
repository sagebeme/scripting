#!/bin/bash
# Exercise 1: Basic Patterns
# Complete the tasks below by adding the appropriate commands

# Create test file
cat > test.txt << EOF
hello world
test123
abc123def
email@example.com
123-456-7890
EOF

# Task 1: Match lines containing digits
# Use grep to find lines with numbers
# Add command here:


# Task 2: Match lines starting with 'hello'
# Use ^ anchor
# Add command here:


# Task 3: Match lines ending with digits
# Use $ anchor
# Add command here:


# Task 4: Match lines with word 'test'
# Use word boundaries
# Add command here:


# Task 5: Match lines with one or more digits
# Use + quantifier (with -E)
# Add command here:


# Task 6: Match lines with zero or more 'a'
# Use * quantifier
# Add command here:


# Task 7: Match lines with exactly 3 digits
# Use {3} quantifier
# Add command here:


# Task 8: Match lines with 2-4 digits
# Use {2,4} quantifier
# Add command here:


# Task 9: Match lines with character class [0-9]
# Add command here:


# Task 10: Match lines NOT containing digits
# Use negated character class or -v
# Add command here:


# Cleanup
rm -f test.txt
echo "Exercise 1 completed! Check your work above."
