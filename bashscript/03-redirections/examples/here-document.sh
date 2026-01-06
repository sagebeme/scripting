#!/bin/bash
# Example 3: Here Document
# Create scripts using here documents

echo "=== Here Document Examples ==="
echo ""

# Example 1: Basic here document
echo "1. Creating file with here document:"
cat > example1.txt << EOF
Line 1: Hello
Line 2: World
Line 3: From Here Document
EOF
cat example1.txt
echo ""

# Example 2: Here document with variables
name="Bash Scripting"
echo "2. Here document with variable expansion:"
cat > example2.txt << EOF
Welcome to $name
Today is $(date)
Your home directory is $HOME
EOF
cat example2.txt
echo ""

# Example 3: Here document without variable expansion
echo "3. Here document without expansion (single quotes in delimiter):"
cat > example3.txt << 'EOF'
Variable $name will not expand
Command $(date) will not execute
EOF
cat example3.txt
echo ""

# Example 4: Here string
echo "4. Here string example:"
wc -w <<< "This is a test string with multiple words"
echo ""

# Example 5: Feed here document to command
echo "5. Feeding here document to command:"
sort << EOF
zebra
apple
banana
EOF
echo ""

# Cleanup
rm -f example1.txt example2.txt example3.txt
