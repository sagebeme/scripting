#!/bin/bash
# Example 2: sed Examples
# Demonstrate sed text processing

echo "=== sed Examples ==="
echo ""

# Create test file
cat > test.txt << EOF
hello world
test123
abc123def
replace me
multiple replace replace
line to delete
keep this line
EOF

echo "1. Original file:"
cat test.txt
echo ""

echo "2. Replace first occurrence:"
sed 's/replace/changed/' test.txt
echo ""

echo "3. Replace all occurrences:"
sed 's/replace/changed/g' test.txt
echo ""

echo "4. Delete lines containing 'delete':"
sed '/delete/d' test.txt
echo ""

echo "5. Print only lines matching pattern:"
sed -n '/test/p' test.txt
echo ""

echo "6. Replace on specific line (line 2):"
sed '2s/test/TEST/' test.txt
echo ""

echo "7. Multiple substitutions:"
sed -e 's/hello/HELLO/' -e 's/world/WORLD/' test.txt
echo ""

echo "8. In-place editing (simulated):"
sed 's/replace/CHANGED/g' test.txt > test_modified.txt
cat test_modified.txt
echo ""

# Cleanup
rm -f test.txt test_modified.txt
