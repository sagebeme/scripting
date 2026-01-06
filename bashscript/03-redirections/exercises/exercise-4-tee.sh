#!/bin/bash
# Exercise 4: tee Command
# Complete the tasks below by adding the appropriate commands

# Task 1: Display output and save to file using tee
# List files and save to filelist.txt
# Add command here:


# Task 2: Append to file using tee -a
# Add date to filelist.txt (append, don't overwrite)
# Add command here:


# Task 3: Use tee in a pipeline
# Sort data and save to file while displaying
# Create test data first:
echo -e "zebra\napple\nbanana" > testdata.txt
# Now sort, display, and save
# Add command here:


# Task 4: Use tee to save to multiple files
# Display output and save to both file1.txt and file2.txt
# Add command here:


# Task 5: Combine tee with other commands
# Count lines, display count, and save to file
# Add command here:


# Task 6: Use tee with error redirection
# Run a command, save output, and handle errors
# Add command here:


# Cleanup
rm -f filelist.txt testdata.txt file1.txt file2.txt
echo "Exercise 4 completed! Check your work above."
