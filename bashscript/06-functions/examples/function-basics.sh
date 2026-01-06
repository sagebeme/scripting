#!/bin/bash
# Example 1: Function Basics
# Demonstrate function definition and calling

echo "=== Function Basics ==="
echo ""

# Simple function
greet() {
    echo "Hello from function!"
}

echo "1. Simple function:"
greet
echo ""

# Function with parameters
greet_user() {
    local name=$1
    echo "Hello, $name!"
}

echo "2. Function with parameter:"
greet_user "Bash Learner"
echo ""

# Function that returns data
get_date() {
    date +"%Y-%m-%d"
}

echo "3. Function returning data:"
current_date=$(get_date)
echo "Today is: $current_date"
echo ""

# Function with return code
check_file() {
    local file=$1
    if [ -f "$file" ]; then
        return 0
    else
        return 1
    fi
}

echo "4. Function with return code:"
touch test.txt
if check_file "test.txt"; then
    echo "File exists!"
fi
rm -f test.txt
echo ""

# Function with multiple parameters
add() {
    local a=$1
    local b=$2
    echo $((a + b))
}

echo "5. Function with multiple parameters:"
result=$(add 5 3)
echo "5 + 3 = $result"
echo ""

# Function with default behavior
display_info() {
    local name=${1:-"Guest"}
    local age=${2:-0}
    echo "Name: $name, Age: $age"
}

echo "6. Function with default parameters:"
display_info
display_info "John" 25
