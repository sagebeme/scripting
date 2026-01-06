#!/bin/bash
# Exercise 1: Basic Redirections
# Complete the tasks below by adding the appropriate commands

# Create test directory
mkdir -p redir_exercise
cd redir_exercise
echo "Test content" > testfile.txt

# Task 1: Redirect output of 'ls' to a file called 'filelist.txt'
# Add command here:


# Task 2: Append the date to 'filelist.txt'
# Add command here:


# Task 3: Redirect errors from a non-existent command to 'errors.log'
# Hint: ls nonexistent 2> errors.log
# Add command here:


# Task 4: Redirect both stdout and stderr to 'output.log'
# Add command here:


# Task 5: Redirect stdout to 'out.log' and stderr to 'err.log'
# Add command here:


# Task 6: Discard output (send to /dev/null)
# Add command here:


# Task 7: Redirect input from 'testfile.txt' to 'cat' command
# Add command here:


# Task 8: Combine input and output redirection
# Read from testfile.txt and write to output.txt
# Add command here:


cd ..
rm -rf redir_exercise
echo "Exercise 1 completed! Check your work above."
