#!/bin/bash
# Example 3: Ownership Manager
# Change ownership with validation

file="$1"
new_owner="$2"
new_group="$3"

if [ $# -lt 2 ]; then
    echo "Usage: $0 <file> <owner> [group]"
    echo "Example: $0 file.txt john"
    echo "Example: $0 file.txt john developers"
    exit 1
fi

if [ ! -e "$file" ]; then
    echo "Error: $file does not exist"
    exit 1
fi

# Display current ownership
echo "Current ownership:"
ls -l "$file"
echo ""

# Check if owner exists
if ! id "$new_owner" &>/dev/null; then
    echo "Warning: User '$new_owner' may not exist"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Change ownership
if [ -n "$new_group" ]; then
    # Change both owner and group
    echo "Changing ownership to $new_owner:$new_group"
    chown "$new_owner:$new_group" "$file"
else
    # Change only owner
    echo "Changing ownership to $new_owner"
    chown "$new_owner" "$file"
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "New ownership:"
    ls -l "$file"
    echo ""
    echo "Ownership changed successfully!"
else
    echo ""
    echo "Error: Failed to change ownership"
    echo "You may need sudo privileges"
    exit 1
fi
