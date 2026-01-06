#!/bin/bash
# Example 1: grep Examples
# Demonstrate various grep patterns

echo "=== grep Examples ==="
echo ""

# Create test file
cat > test.txt << EOF
Error: connection failed
Warning: low memory
Info: process started
ERROR: timeout occurred
error: invalid input
Success: operation completed
EOF

echo "1. Basic search:"
grep "Error" test.txt
echo ""

echo "2. Case-insensitive:"
grep -i "error" test.txt
echo ""

echo "3. Invert match:"
grep -v "Error" test.txt
echo ""

echo "4. With line numbers:"
grep -n "Error" test.txt
echo ""

echo "5. Extended regex (Error or Warning):"
grep -E "Error|Warning" test.txt
echo ""

echo "6. Count matches:"
grep -c "Error" test.txt
echo ""

echo "7. Whole words only:"
grep -w "Error" test.txt
echo ""

echo "8. Context (2 lines before and after):"
grep -B 2 -A 2 "Warning" test.txt
echo ""

# Cleanup
rm -f test.txt
