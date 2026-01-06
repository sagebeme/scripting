#!/bin/bash
# Example 3: Directory Lister
# Description: List files in current directory with details and count

echo "=== Files in Current Directory ==="
ls -lh
echo ""
echo "Total files and directories: $(ls -1 | wc -l)"
echo ""
echo "Hidden files:"
ls -la | grep "^\." | wc -l
