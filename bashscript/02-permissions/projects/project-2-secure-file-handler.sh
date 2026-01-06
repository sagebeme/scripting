#!/bin/bash
# Project 2: Secure File Handler
# 
# Instructions:
# Create a script that handles files with secure default permissions
# 
# Requirements:
# 1. Create files with secure default permissions
# 2. Protect sensitive files (600)
# 3. Make scripts executable (755)
# 4. Handle directory permissions appropriately
# 5. Set umask for secure defaults

# TODO: Add your code below

echo "Secure File Handler"
echo "==================="

# Step 1: Save current umask
# Add code here:


# Step 2: Set secure umask (e.g., 077 or 027)
# Add code here:


# Step 3: Create a function to create secure files
# Function should:
# - Take filename and permission type as parameters
# - Create file with appropriate permissions
# - Verify permissions were set correctly
# Add code here:


# Step 4: Create different types of files
# - Sensitive file (600): private data
# - Script file (755): executable script
# - Regular file (644): normal file
# - Directory (755): standard directory
# Add code here:


# Step 5: Display created files and their permissions
# Add code here:


# Step 6: Restore original umask
# Add code here:


echo ""
echo "Secure files created successfully!"
