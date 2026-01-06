#!/bin/bash
# Example 2: Pipe Examples
# Demonstrate various pipe patterns and filters

echo "=== Pipe Examples ==="
echo ""

# Create sample data
cat > data.txt << EOF
apple
banana
apple
cherry
banana
date
grape
apple
EOF

echo "Sample data:"
cat data.txt
echo ""

# Example 1: Simple pipe
echo "1. Count lines:"
cat data.txt | wc -l
echo ""

# Example 2: Filter with grep
echo "2. Find 'apple':"
cat data.txt | grep apple
echo ""

# Example 3: Sort
echo "3. Sorted:"
cat data.txt | sort
echo ""

# Example 4: Sort and unique
echo "4. Sorted and unique:"
cat data.txt | sort | uniq
echo ""

# Example 5: Count occurrences
echo "5. Count 'apple' occurrences:"
cat data.txt | grep -c apple
echo ""

# Example 6: First few lines
echo "6. First 3 lines:"
cat data.txt | head -3
echo ""

# Example 7: Last few lines
echo "7. Last 2 lines:"
cat data.txt | tail -2
echo ""

# Example 8: Complex pipeline
echo "8. Complex: sort, unique, count:"
cat data.txt | sort | uniq | wc -l
echo ""

# Example 9: Filter and transform
echo "9. Lines with 'a', sorted:"
cat data.txt | grep a | sort
echo ""

# Cleanup
rm -f data.txt
