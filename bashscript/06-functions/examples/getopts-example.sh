#!/bin/bash
# Example 2: getopts Example
# Demonstrate option parsing with getopts

usage() {
    echo "Usage: $0 [-a] [-b] [-c value] [-h] [files...]"
    echo "  -a    Enable option a"
    echo "  -b    Enable option b"
    echo "  -c    Option c with value"
    echo "  -h    Show this help"
    exit 1
}

# Initialize flags
flag_a=false
flag_b=false
value_c=""

# Parse options
while getopts "abc:h" opt; do
    case $opt in
        a)
            flag_a=true
            echo "Option a enabled"
            ;;
        b)
            flag_b=true
            echo "Option b enabled"
            ;;
        c)
            value_c="$OPTARG"
            echo "Option c with value: $value_c"
            ;;
        h)
            usage
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
    esac
done

# Shift to get remaining arguments
shift $((OPTIND-1))

# Display flags
echo ""
echo "Flags:"
echo "  flag_a: $flag_a"
echo "  flag_b: $flag_b"
echo "  value_c: $value_c"

# Process remaining arguments
if [ $# -gt 0 ]; then
    echo ""
    echo "Remaining arguments:"
    for arg in "$@"; do
        echo "  - $arg"
    done
fi
