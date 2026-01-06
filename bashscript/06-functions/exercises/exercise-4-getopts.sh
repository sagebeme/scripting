#!/bin/bash
# Exercise 4: getopts
# Complete the tasks below by adding the appropriate commands
# Run with: ./exercise-4-getopts.sh -a -b -c value

# Task 1: Use getopts to parse options 'a', 'b', and 'c' (c requires value)
# Add getopts loop here:


# Task 2: Handle option 'a' - display "Option a selected"
# Add case for 'a' here:


# Task 3: Handle option 'b' - display "Option b selected"
# Add case for 'b' here:


# Task 4: Handle option 'c' - display "Option c with value: [value]"
# Use $OPTARG for the value
# Add case for 'c' here:


# Task 5: Handle invalid options - display error message
# Add case for '?' here:


# Task 6: After getopts, shift to remove processed options
# Add shift command here:


# Task 7: Display remaining positional arguments
# Add code here:


# Task 8: Add help option 'h' that displays usage
# Add case for 'h' here:


# Task 9: Create a usage function
# Function should display script usage
# Add function definition here:


# Task 10: Call usage function when -h is used
# Add function call in case 'h' here:


echo "Exercise 4 completed! Check your work above."
echo "Try: ./exercise-4-getopts.sh -a -b -c test remaining args"
