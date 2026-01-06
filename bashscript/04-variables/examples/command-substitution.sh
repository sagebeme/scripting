#!/bin/bash
# Example 3: Command Substitution
# Use command output in scripts

echo "=== Command Substitution Examples ==="
echo ""

# Modern syntax (preferred)
current_date=$(date)
echo "1. Current date: $current_date"
echo ""

# Legacy syntax
current_user=`whoami`
echo "2. Current user: $current_user"
echo ""

# Store file list
files=$(ls)
echo "3. Files in directory:"
echo "$files"
echo ""

# Count files
file_count=$(ls -1 | wc -l)
echo "4. File count: $file_count"
echo ""

# System information
system_info=$(uname -a)
echo "5. System info: $system_info"
echo ""

# Nested command substitution
line_count=$(echo "$files" | wc -l)
echo "6. Number of files (nested): $line_count"
echo ""

# In echo statement
echo "7. Current directory: $(pwd)"
echo ""

# With arithmetic
file_count_doubled=$((file_count * 2))
echo "8. File count doubled: $file_count_doubled"
echo ""

# Command that might fail
result=$(ls nonexistent 2>&1)
echo "9. Error handling: $result"
