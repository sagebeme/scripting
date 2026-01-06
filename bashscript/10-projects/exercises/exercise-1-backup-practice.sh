#!/bin/bash
# Exercise 1: Backup Practice
# Complete the tasks below to practice backup concepts

# Create test directory structure
mkdir -p backup_practice/{source,backups}
echo "File 1 content" > backup_practice/source/file1.txt
echo "File 2 content" > backup_practice/source/file2.txt

# Task 1: Create a backup directory with timestamp
# Format: backup_YYYYMMDD_HHMMSS
# Add command here:


# Task 2: Copy source files to backup directory
# Add command here:


# Task 3: Compress the backup directory to .tar.gz
# Add command here:


# Task 4: Verify the backup was created successfully
# Check if compressed file exists
# Add command here:


# Task 5: List all backups with sizes
# Add command here:


# Task 6: Create a function to clean old backups
# Function should keep only the 3 most recent backups
# Add function definition here:


# Task 7: Call the cleanup function
# Add function call here:


# Task 8: Create a backup verification function
# Function should check backup integrity
# Add function definition here:


# Task 9: Verify the latest backup
# Add function call here:


# Task 10: Display backup summary
# Show: total backups, total size, oldest, newest
# Add summary code here:


# Cleanup
rm -rf backup_practice
echo "Exercise 1 completed! Check your work above."
