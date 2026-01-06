#!/bin/bash
# Example 3: awk Examples
# Demonstrate awk data processing

echo "=== awk Examples ==="
echo ""

# Create test file
cat > data.txt << EOF
John 25 Engineer 50000
Jane 30 Doctor 80000
Bob 28 Teacher 45000
Alice 32 Lawyer 90000
EOF

echo "1. Original data:"
cat data.txt
echo ""

echo "2. Print first field (name):"
awk '{print $1}' data.txt
echo ""

echo "3. Print name and salary:"
awk '{print $1, $4}' data.txt
echo ""

echo "4. Filter by age > 28:"
awk '$2 > 28 {print $1, $2}' data.txt
echo ""

echo "5. Calculate total salary:"
awk '{sum+=$4} END {print "Total salary:", sum}' data.txt
echo ""

echo "6. Calculate average age:"
awk '{sum+=$2; count++} END {print "Average age:", sum/count}' data.txt
echo ""

echo "7. Formatted output:"
awk '{printf "%-10s %-5s %-10s $%d\n", $1, $2, $3, $4}' data.txt
echo ""

echo "8. Custom field separator:"
echo "name:age:job" > custom.txt
echo "John:25:Engineer" >> custom.txt
awk -F: '{print $1, "is", $3}' custom.txt
echo ""

echo "9. Pattern matching:"
awk '/Engineer/ {print $1, "is an engineer"}' data.txt
echo ""

echo "10. Conditional formatting:"
awk '{if ($4 > 60000) print $1, "has high salary"; else print $1, "has normal salary"}' data.txt
echo ""

# Cleanup
rm -f data.txt custom.txt
