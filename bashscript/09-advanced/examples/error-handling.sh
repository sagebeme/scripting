#!/bin/bash
# Example 2: Error Handling
# Demonstrate error handling best practices

echo "=== Error Handling Examples ==="
echo ""

# Set error handling
set -e  # Exit on error
set -u  # Error on unset variables
set -o pipefail  # Fail on pipe errors

# Error handling function
handle_error() {
    local line=$1
    echo "Error occurred at line $line" >&2
    exit 1
}

trap 'handle_error $LINENO' ERR

echo "1. Error handling enabled:"
echo "   set -e: Exit on error"
echo "   set -u: Error on unset variables"
echo "   set -o pipefail: Fail on pipe errors"
echo ""

# Safe command execution
safe_command() {
    local cmd=$1
    if eval "$cmd" 2>/dev/null; then
        echo "2. Command succeeded: $cmd"
    else
        echo "2. Command failed: $cmd (handled gracefully)"
        return 1
    fi
}

safe_command "echo 'test'"
safe_command "ls nonexistent 2>/dev/null || true"
echo ""

# Error checking
check_file() {
    local file=$1
    if [ ! -f "$file" ]; then
        echo "3. Error: File '$file' not found" >&2
        return 1
    fi
    echo "3. File '$file' exists"
}

touch test.txt
check_file "test.txt"
check_file "nonexistent.txt" || true
echo ""

# Cleanup
rm -f test.txt

# Disable strict mode for demonstration
set +e
set +u
set +o pipefail

echo "4. Error handling disabled for script continuation"
