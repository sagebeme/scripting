#!/bin/bash
# Example 1: Permission Viewer
# Display detailed permission information for files

echo "=== Permission Viewer ==="
echo ""

# Check if file/directory provided as argument
if [ $# -eq 0 ]; then
    target="."
else
    target="$1"
fi

if [ ! -e "$target" ]; then
    echo "Error: $target does not exist"
    exit 1
fi

echo "Permissions for: $target"
echo ""

# Display detailed information
ls -ld "$target"
echo ""

# Parse permissions
perms=$(stat -c "%a" "$target" 2>/dev/null || stat -f "%OLp" "$target" 2>/dev/null)
echo "Octal: $perms"
echo ""

# Display owner and group
owner=$(stat -c "%U" "$target" 2>/dev/null || stat -f "%Su" "$target" 2>/dev/null)
group=$(stat -c "%G" "$target" 2>/dev/null || stat -f "%Sg" "$target" 2>/dev/null)
echo "Owner: $owner"
echo "Group: $group"
echo ""

# Check special permissions
if [ -f "$target" ]; then
    if [ -u "$target" ]; then
        echo "SUID: Set"
    fi
    if [ -g "$target" ]; then
        echo "SGID: Set"
    fi
fi

if [ -d "$target" ]; then
    if [ -k "$target" ]; then
        echo "Sticky bit: Set"
    fi
    if [ -g "$target" ]; then
        echo "SGID: Set"
    fi
fi
