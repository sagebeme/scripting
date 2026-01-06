#!/bin/bash
# Example 2: System Information
# Description: Display basic system information using command substitution

echo "=== System Information ==="
echo ""
echo "Current User: $(whoami)"
echo "Current Directory: $(pwd)"
echo "Date and Time: $(date)"
echo "System Information: $(uname -a)"
echo ""
echo "Home Directory: $HOME"
echo "Shell: $SHELL"
