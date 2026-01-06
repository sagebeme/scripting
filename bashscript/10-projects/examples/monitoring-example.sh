#!/bin/bash
# Example 2: System Monitoring Example
# Demonstrate system monitoring concepts

echo "=== System Monitoring Example ==="
echo ""

# Function to get system info
get_system_info() {
    echo "1. System Information:"
    echo "   CPU Usage: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')"
    echo "   Memory Usage:"
    free -h | grep Mem | awk '{print "     Used: " $3 " / " $2 " (" $3/$2*100 "%)"}'
    echo "   Disk Usage:"
    df -h / | tail -1 | awk '{print "     Used: " $3 " / " $2 " (" $5 ")"}'
    echo ""
}

# Function to check process
check_process() {
    local process=$1
    if pgrep -x "$process" > /dev/null; then
        echo "   ✓ Process '$process' is running"
        return 0
    else
        echo "   ✗ Process '$process' is NOT running"
        return 1
    fi
}

get_system_info

echo "2. Process Monitoring:"
check_process "bash"
check_process "systemd"
check_process "nonexistent_process"
echo ""

# Function to check disk space threshold
check_disk_space() {
    local threshold=80
    local usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    
    echo "3. Disk Space Alert:"
    if [ $usage -gt $threshold ]; then
        echo "   ⚠ WARNING: Disk usage is ${usage}% (threshold: ${threshold}%)"
    else
        echo "   ✓ Disk usage is ${usage}% (below threshold)"
    fi
    echo ""
}

check_disk_space

# Function to generate report
generate_report() {
    local report_file="system_report_$(date +%Y%m%d_%H%M%S).txt"
    
    {
        echo "System Report - $(date)"
        echo "========================"
        echo ""
        echo "CPU Information:"
        lscpu | grep "Model name"
        echo ""
        echo "Memory:"
        free -h
        echo ""
        echo "Disk:"
        df -h
        echo ""
        echo "Running Processes:"
        ps aux | head -10
    } > "$report_file"
    
    echo "4. Report Generated:"
    echo "   File: $report_file"
    echo "   Size: $(du -h "$report_file" | cut -f1)"
    echo ""
    
    # Cleanup
    rm -f "$report_file"
}

generate_report

echo "Example completed!"
