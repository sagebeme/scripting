#!/bin/bash
# Example 1: Background Processes
# Demonstrate running commands in background

echo "=== Background Processes ==="
echo ""

# Run command in background
echo "1. Running sleep in background:"
sleep 5 &
BG_PID=$!
echo "Background PID: $BG_PID"
echo ""

# List jobs
echo "2. Current jobs:"
jobs
echo ""

# Wait for background job
echo "3. Waiting for background job..."
wait $BG_PID
echo "Background job completed"
echo ""

# Multiple background jobs
echo "4. Starting multiple background jobs:"
for i in {1..3}; do
    sleep 2 &
    echo "Started job $i (PID: $!)"
done
echo ""

# Wait for all background jobs
echo "5. Waiting for all jobs..."
wait
echo "All jobs completed"
echo ""

# nohup example
echo "6. Using nohup:"
nohup sleep 3 > nohup.out 2>&1 &
echo "Started with nohup (PID: $!)"
sleep 1
echo "Process still running after terminal would close"
kill $! 2>/dev/null
rm -f nohup.out
