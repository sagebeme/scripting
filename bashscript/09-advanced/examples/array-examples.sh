#!/bin/bash
# Example 1: Array Examples
# Demonstrate array operations

echo "=== Array Examples ==="
echo ""

# Indexed array
arr=(apple banana cherry)
echo "1. Indexed array:"
echo "   Elements: ${arr[@]}"
echo "   First element: ${arr[0]}"
echo "   Length: ${#arr[@]}"
echo ""

# Add element
arr+=(date)
echo "2. After adding element:"
echo "   ${arr[@]}"
echo ""

# Iterate array
echo "3. Iterating array:"
for item in "${arr[@]}"; do
    echo "   - $item"
done
echo ""

# Associative array
declare -A assoc
assoc[name]="John"
assoc[age]=30
assoc[job]="Engineer"

echo "4. Associative array:"
for key in "${!assoc[@]}"; do
    echo "   $key: ${assoc[$key]}"
done
echo ""

# Array slicing
echo "5. Array slice (first 2 elements):"
echo "   ${arr[@]:0:2}"
echo ""

# Array operations
numbers=(1 2 3 4 5)
echo "6. Array operations:"
echo "   Original: ${numbers[@]}"
echo "   Reversed indices: ${numbers[@]: -1} ${numbers[@]:0:4}"
echo ""
