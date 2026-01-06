#!/bin/bash
# Example 1: Backup System Example
# Demonstrate backup system concepts

echo "=== Backup System Example ==="
echo ""

# Create sample files to backup
mkdir -p backup_demo/source
echo "Important data 1" > backup_demo/source/file1.txt
echo "Important data 2" > backup_demo/source/file2.txt

# Create backup directory with timestamp
timestamp=$(date +%Y%m%d_%H%M%S)
backup_dir="backup_demo/backup_$timestamp"
mkdir -p "$backup_dir"

echo "1. Creating backup:"
echo "   Source: backup_demo/source"
echo "   Backup: $backup_dir"
cp -r backup_demo/source/* "$backup_dir/"
echo "   Backup created successfully"
echo ""

# Compress backup
echo "2. Compressing backup:"
tar -czf "${backup_dir}.tar.gz" "$backup_dir"
echo "   Compressed: ${backup_dir}.tar.gz"
echo ""

# List backups
echo "3. Available backups:"
ls -lh backup_demo/backup_*.tar.gz 2>/dev/null | awk '{print "   " $9, "(" $5 ")"}'
echo ""

# Cleanup old backups (keep only 2)
echo "4. Cleaning old backups (keeping 2 most recent):"
backup_count=$(ls backup_demo/backup_*.tar.gz 2>/dev/null | wc -l)
if [ $backup_count -gt 2 ]; then
    ls -t backup_demo/backup_*.tar.gz | tail -n +3 | xargs rm -f
    echo "   Old backups removed"
else
    echo "   No cleanup needed"
fi
echo ""

# Verify backup
echo "5. Verifying backup:"
if [ -f "${backup_dir}.tar.gz" ]; then
    echo "   Backup verification: SUCCESS"
    echo "   Backup size: $(du -h "${backup_dir}.tar.gz" | cut -f1)"
else
    echo "   Backup verification: FAILED"
fi
echo ""

# Cleanup demo
rm -rf backup_demo
echo "Example completed!"
