#!/bin/bash
# Example 2: Signal Handling
# Demonstrate signal handling with trap

cleanup() {
    echo ""
    echo "Cleaning up..."
    # Remove temporary files
    rm -f /tmp/temp_*.txt
    echo "Cleanup complete"
}

# Trap signals
trap cleanup INT TERM EXIT

echo "=== Signal Handling ==="
echo ""

# Create temporary file
touch /tmp/temp_$$.txt
echo "Created temporary file: /tmp/temp_$$.txt"
echo ""

# Signal handler function
handle_signal() {
    local sig=$1
    echo "Received signal: $sig"
    cleanup
    exit 1
}

# Trap specific signals
trap 'handle_signal INT' INT
trap 'handle_signal TERM' TERM

echo "1. Script is running..."
echo "2. Press Ctrl+C to test SIGINT handling"
echo "3. Or wait 10 seconds for normal exit"
echo ""

# Simulate work
for i in {1..10}; do
    echo -n "."
    sleep 1
done

echo ""
echo "Script completed normally"
