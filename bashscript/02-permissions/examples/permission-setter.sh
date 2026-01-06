#!/bin/bash
# Example 2: Permission Setter
# Safely set permissions using different methods

file="$1"
mode="$2"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <file> <mode>"
    echo "Mode can be:"
    echo "  - Octal: 755, 644, 600, etc."
    echo "  - Symbolic: u+x, g-w, a=r, etc."
    exit 1
fi

if [ ! -e "$file" ]; then
    echo "Error: $file does not exist"
    exit 1
fi

# Display current permissions
echo "Current permissions:"
ls -l "$file"
echo ""

# Check if mode is octal (all digits) or symbolic
if [[ "$mode" =~ ^[0-7]{3,4}$ ]]; then
    # Octal notation
    echo "Setting permissions using octal notation: $mode"
    chmod "$mode" "$file"
else
    # Symbolic notation
    echo "Setting permissions using symbolic notation: $mode"
    chmod "$mode" "$file"
fi

# Display new permissions
echo ""
echo "New permissions:"
ls -l "$file"

# Verify
if [ $? -eq 0 ]; then
    echo ""
    echo "Permissions updated successfully!"
else
    echo ""
    echo "Error: Failed to update permissions"
    exit 1
fi
