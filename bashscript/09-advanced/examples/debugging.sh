#!/bin/bash
# Example 3: Debugging
# Demonstrate debugging techniques

echo "=== Debugging Examples ==="
echo ""

# Enable tracing
echo "1. Execution tracing (set -x):"
set -x
test_var="debug test"
result=$((5 + 3))
set +x
echo "   Result: $result"
echo ""

# Debug function
debug() {
    if [ "${DEBUG:-0}" = "1" ]; then
        echo "[DEBUG] $*" >&2
    fi
}

echo "2. Conditional debugging:"
DEBUG=1 debug "This is a debug message"
DEBUG=0 debug "This won't be shown"
echo ""

# Verbose mode
verbose() {
    local msg=$1
    if [ "${VERBOSE:-0}" = "1" ]; then
        echo "[VERBOSE] $msg"
    fi
}

echo "3. Verbose mode:"
VERBOSE=1 verbose "Verbose message shown"
VERBOSE=0 verbose "Verbose message hidden"
echo ""

# Function tracing
trace_function() {
    echo "4. Function entry: ${FUNCNAME[0]}"
    echo "   Called from: ${FUNCNAME[1]}"
    local local_var="local value"
    echo "   Local variable: $local_var"
    echo "   Function exit: ${FUNCNAME[0]}"
}

trace_function
echo ""

# Error location
check_error_location() {
    local line=$1
    echo "5. Error occurred at line: $line"
    echo "   Function: ${FUNCNAME[1]}"
    echo "   Script: ${BASH_SOURCE[0]}"
}

# Simulate error check
check_error_location $LINENO
echo ""

echo "6. Debugging tips:"
echo "   - Use 'set -x' for execution tracing"
echo "   - Use 'set -e' to exit on errors"
echo "   - Use 'set -u' to catch unset variables"
echo "   - Use DEBUG/VERBOSE flags for conditional output"
echo "   - Check \$LINENO for error location"
