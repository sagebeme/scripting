#!/bin/bash
# Exercise 3: Log Rotation Practice
# Complete the tasks below to practice log rotation

# Create test log file
mkdir -p log_practice
for i in {1..50}; do
    echo "$(date): Log entry $i" >> log_practice/app.log
done

# Task 1: Check log file size
# Add command here:


# Task 2: Create rotated log filename with timestamp
# Format: app.log.YYYYMMDD_HHMMSS
# Add command here:


# Task 3: Rotate log file (rename current log)
# Add command here:


# Task 4: Create new empty log file
# Add command here:


# Task 5: Compress the rotated log file
# Add command here:


# Task 6: List all rotated log files
# Add command here:


# Task 7: Create function to rotate log if size > threshold
# Function should take logfile and size threshold as parameters
# Add function definition here:


# Task 8: Call rotation function for app.log with 1KB threshold
# Add function call here:


# Task 9: Create function to clean old logs
# Keep only last N rotated logs
# Add function definition here:


# Task 10: Clean old logs (keep only 3)
# Add function call here:


# Cleanup
rm -rf log_practice
echo "Exercise 3 completed! Check your work above."
