#!/bin/bash
# Example 1: Conditional Examples
# Demonstrate various if/else patterns

echo "=== Conditional Examples ==="
echo ""

# Basic if
file="test.txt"
touch "$file"
if [ -f "$file" ]; then
    echo "1. File exists: $file"
fi
echo ""

# If/else
if [ -d "$file" ]; then
    echo "It's a directory"
else
    echo "2. It's not a directory"
fi
echo ""

# If/elif/else
num=5
if [ $num -gt 10 ]; then
    echo "Greater than 10"
elif [ $num -gt 5 ]; then
    echo "Greater than 5"
else
    echo "3. Number is 5 or less"
fi
echo ""

# String comparison
str="hello"
if [ "$str" = "hello" ]; then
    echo "4. String matches"
fi
echo ""

# File tests
if [ -r "$file" ] && [ -w "$file" ]; then
    echo "5. File is readable and writable"
fi
echo ""

# Multiple conditions
if [ -f "$file" ] || [ -d "$file" ]; then
    echo "6. File or directory exists"
fi
echo ""

# Cleanup
rm -f "$file"
