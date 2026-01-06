#!/bin/bash
# Project 3: Basic Backup Script
# 
# Instructions:
# Create a backup script that copies files to a backup directory
# 
# Requirements:
# 1. Take a source directory as input
# 2. Create a backup directory with timestamp
# 3. Copy all files from source to backup
# 4. Display backup location and size
# 5. Show completion message
# 6. Handle errors (directory doesn't exist, etc.)

# TODO: Add your code below

echo "Backup Script"
echo "============"

# Step 1: Get source directory from user
# Hint: Use read or $1
# Add code here:


# Step 2: Check if source directory exists
# Add code here:


# Step 3: Create backup directory with timestamp
# Format: backup_YYYY-MM-DD_HH-MM-SS
# Hint: Use $(date +"%Y-%m-%d_%H-%M-%S")
# Add code here:


# Step 4: Copy files from source to backup
# Hint: Use cp -r for recursive copy
# Add code here:


# Step 5: Display backup information
echo ""
echo "Backup completed!"
echo "Source: $source_dir"
echo "Backup location: $backup_dir"
# Add code to display backup size (use du -sh)


echo ""
echo "Backup finished successfully!"
