#!/bin/bash
# Example 3: Log Rotation Example
# Demonstrate log rotation concepts

echo "=== Log Rotation Example ==="
echo ""

# Create sample log files
mkdir -p log_demo
for i in {1..5}; do
    echo "Log entry $(date) - Entry $i" >> "log_demo/app.log"
    sleep 0.1
done

echo "1. Original log files:"
ls -lh log_demo/
echo ""

# Rotate log file
rotate_log() {
    local log_file=$1
    local max_size=1K  # 1KB for demo
    
    if [ -f "$log_file" ]; then
        local size=$(stat -f%z "$log_file" 2>/dev/null || stat -c%s "$log_file" 2>/dev/null)
        local max_bytes=1024
        
        if [ $size -gt $max_bytes ]; then
            local timestamp=$(date +%Y%m%d_%H%M%S)
            local rotated_file="${log_file}.${timestamp}"
            
            echo "2. Rotating log file:"
            echo "   Original: $log_file ($(du -h "$log_file" | cut -f1))"
            mv "$log_file" "$rotated_file"
            echo "   Rotated to: $rotated_file"
            touch "$log_file"
            echo "   New log file created"
            echo ""
            
            # Compress old log
            echo "3. Compressing old log:"
            gzip "$rotated_file"
            echo "   Compressed: ${rotated_file}.gz"
            echo ""
        else
            echo "2. Log file size OK, no rotation needed"
            echo ""
        fi
    fi
}

# Make log file larger for demo
for i in {1..100}; do
    echo "Log entry $(date) - Entry $i" >> "log_demo/app.log"
done

rotate_log "log_demo/app.log"

# Cleanup old logs (keep last 3)
cleanup_old_logs() {
    local log_dir=$1
    local keep_count=3
    
    echo "4. Cleaning old logs (keeping $keep_count most recent):"
    local log_count=$(ls -t "$log_dir"/*.gz 2>/dev/null | wc -l)
    
    if [ $log_count -gt $keep_count ]; then
        ls -t "$log_dir"/*.gz | tail -n +$((keep_count + 1)) | while read old_log; do
            echo "   Removing: $(basename "$old_log")"
            rm -f "$old_log"
        done
    else
        echo "   No cleanup needed (only $log_count logs)"
    fi
    echo ""
}

cleanup_old_logs "log_demo"

# List final logs
echo "5. Final log files:"
ls -lh log_demo/
echo ""

# Cleanup demo
rm -rf log_demo
echo "Example completed!"
