#!/bin/bash
# Example 2: Parameter Expansion
# Demonstrate various parameter expansion techniques

echo "=== Parameter Expansion Examples ==="
echo ""

# Test variable
text="Hello World Bash Scripting"

# Length
echo "1. Length of 'text': ${#text}"
echo ""

# Default value
unset maybe_set
echo "2. Default value: ${maybe_set:-'not set'}"
maybe_set="I'm set"
echo "   When set: ${maybe_set:-'not set'}"
echo ""

# Assign default
unset assign_test
echo "3. Before assign: ${assign_test:-unset}"
${assign_test:="assigned value"}
echo "   After assign: $assign_test"
echo ""

# Substring
echo "4. Substring (first 5 chars): ${text:0:5}"
echo "   Substring (from index 6): ${text:6}"
echo ""

# Pattern removal (shortest from start)
path="/home/user/documents/file.txt"
echo "5. Remove shortest match: ${path#/}"
echo "   Remove longest match: ${path##*/}"
echo ""

# Pattern removal (from end)
echo "6. Remove from end (shortest): ${path%.*}"
echo "   Remove from end (longest): ${path%/*}"
echo ""

# Pattern replacement
echo "7. Replace first: ${text/Hello/Hi}"
echo "   Replace all: ${text//a/A}"
echo ""

# Use alternate value
var="exists"
echo "8. Alternate (when set): ${var:+'alternate value'}"
unset var
echo "   Alternate (when unset): ${var:+'alternate value'}"
