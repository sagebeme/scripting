#!/bin/bash
# Exercise 5: Process Monitoring
# Complete the tasks below by adding the appropriate commands

# Start a test process
sleep 30 &
TEST_PID=$!

# Task 1: Check if process is running
# Check if TEST_PID is still running
# Add command here:


# Task 2: Get process status
# Display status of TEST_PID
# Add command here:


# Task 3: Monitor process resource usage
# Show CPU and memory usage
# Add command here:


# Task 4: Check process parent and children
# Show process tree for TEST_PID
# Add command here:


# Task 5: Monitor process continuously
# Watch process status (use watch or loop)
# Add command here (commented - would run indefinitely):


# Task 6: Check if process exists by name
# Check if 'sleep' process is running
# Add command here:


# Task 7: Count processes by name
# Count how many 'bash' processes are running
# Add command here:


# Task 8: Monitor process and alert when it stops
# Wait for process to finish and alert
# Add command here:


# Task 9: Get process start time
# Show when TEST_PID started
# Add command here:


# Task 10: Monitor multiple processes
# Check status of multiple PIDs
# Add command here:


# Cleanup
kill $TEST_PID 2>/dev/null
wait $TEST_PID 2>/dev/null
echo "Exercise 5 completed! Check your work above."
