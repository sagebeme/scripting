#!/bin/bash
# Example 3: Case Statement
# Demonstrate case statement usage

echo "=== Case Statement Examples ==="
echo ""

# Simple case
value="apple"
echo "1. Simple case:"
case $value in
    apple)
        echo "   It's an apple"
        ;;
    banana)
        echo "   It's a banana"
        ;;
    *)
        echo "   Unknown fruit"
        ;;
esac
echo ""

# Multiple patterns
echo "2. Multiple patterns:"
choice="yes"
case $choice in
    yes|y|Y|YES)
        echo "   Confirmed"
        ;;
    no|n|N|NO)
        echo "   Denied"
        ;;
    *)
        echo "   Invalid choice"
        ;;
esac
echo ""

# File extension case
echo "3. File extension case:"
filename="document.txt"
extension="${filename##*.}"
case $extension in
    txt)
        echo "   Text file"
        ;;
    sh)
        echo "   Shell script"
        ;;
    pdf)
        echo "   PDF document"
        ;;
    *)
        echo "   Unknown file type"
        ;;
esac
echo ""

# Command case
echo "4. Command case:"
cmd="start"
case $cmd in
    start)
        echo "   Starting service..."
        ;;
    stop)
        echo "   Stopping service..."
        ;;
    restart)
        echo "   Restarting service..."
        ;;
    status)
        echo "   Checking status..."
        ;;
    *)
        echo "   Unknown command: $cmd"
        ;;
esac
echo ""

# Pattern matching
echo "5. Pattern matching:"
number=42
case $number in
    [0-9]|[1-9][0-9])
        echo "   Single or double digit"
        ;;
    [1-9][0-9][0-9])
        echo "   Three digit number"
        ;;
    *)
        echo "   Other number"
        ;;
esac
