#!/bin/bash
# Example 1: Basic Redirections
# Demonstrate output and input redirection

echo "=== Basic Redirections Examples ==="
echo ""

# Output redirection (overwrite)
echo "This goes to file" > output.txt
echo "File created with content"

# Output redirection (append)
echo "This is appended" >> output.txt
echo "Content appended"

# Input redirection
echo "Reading from file:"
cat < output.txt
echo ""

# Error redirection
echo "Testing error redirection:"
ls nonexistent_file 2> error.log 2>&1 || echo "Error captured in error.log"
echo ""

# Discard output
echo "Discarding output:"
ls > /dev/null
echo "Output discarded (no output shown)"
echo ""

# Combine stdout and stderr
echo "Combining streams:"
(echo "stdout message"; echo "stderr message" >&2) &> combined.log
cat combined.log
echo ""

# Cleanup
rm -f output.txt error.log combined.log
