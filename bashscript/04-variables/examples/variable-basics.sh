#!/bin/bash
# Example 1: Variable Basics
# Demonstrate variable creation and usage

echo "=== Variable Basics ==="
echo ""

# Basic variable assignment
name="Bash Learner"
age=25
message="Hello World"

echo "Name: $name"
echo "Age: $age"
echo "Message: $message"
echo ""

# Using ${} syntax (preferred)
echo "Name (with braces): ${name}"
echo ""

# Concatenation
first="Hello"
second="Bash"
greeting="${first} ${second}"
echo "Greeting: $greeting"
echo ""

# Variable with spaces (requires quotes)
full_name="John Doe"
echo "Full name: $full_name"
echo ""

# Unsetting variables
temp_var="temporary"
echo "Before unset: $temp_var"
unset temp_var
echo "After unset: ${temp_var:-'variable is unset'}"
echo ""

# Variable scope
local_var="I'm local"
echo "Local variable: $local_var"
