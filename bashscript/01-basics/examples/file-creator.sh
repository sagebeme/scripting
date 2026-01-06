#!/bin/bash
# Example 4: File Creator
# Description: Create a file with content and display it

# Create a file
filename="example.txt"

# Add content to file
echo "This is line 1" > "$filename"
echo "This is line 2" >> "$filename"
echo "This is line 3" >> "$filename"

# Display file contents
echo "Contents of $filename:"
cat "$filename"

# Display file information
echo ""
echo "File information:"
ls -lh "$filename"
