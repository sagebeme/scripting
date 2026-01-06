#!/bin/bash
# Example 2: Loop Examples
# Demonstrate different loop types and patterns

echo "=== Loop Examples ==="
echo ""

# For loop with list
echo "1. For loop with list:"
for item in apple banana cherry; do
    echo "  - $item"
done
echo ""

# For loop with files
echo "2. For loop with files:"
touch file1.txt file2.txt
for file in *.txt; do
    echo "  Found: $file"
done
echo ""

# C-style for loop
echo "3. C-style for loop:"
for ((i=1; i<=5; i++)); do
    echo "  Count: $i"
done
echo ""

# While loop
echo "4. While loop:"
count=1
while [ $count -le 3 ]; do
    echo "  While count: $count"
    ((count++))
done
echo ""

# While reading file
echo "5. While reading file:"
echo -e "line1\nline2\nline3" > testfile.txt
while IFS= read -r line; do
    echo "  Line: $line"
done < testfile.txt
echo ""

# Until loop
echo "6. Until loop:"
num=1
until [ $num -gt 3 ]; do
    echo "  Until count: $num"
    ((num++))
done
echo ""

# Loop with break
echo "7. Loop with break:"
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo "  Count: $i"
done
echo ""

# Loop with continue
echo "8. Loop with continue (skip evens):"
for i in {1..5}; do
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    echo "  Odd: $i"
done
echo ""

# Cleanup
rm -f file*.txt testfile.txt
