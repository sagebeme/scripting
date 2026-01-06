# Projects - Level 1: Basics

## 🎯 Project Overview

These projects will help you apply what you've learned in the exercises. Each project builds on the concepts covered in this module.

## 📋 Project List

### Project 1: Simple File Organizer
**Difficulty**: ⭐⭐ (Beginner)

**Description**: Create a script that automatically organizes files by their extension into appropriate directories.

**Requirements**:
- Create directories: `documents`, `images`, `scripts`
- Move `.txt` files to `documents/`
- Move `.jpg` and `.png` files to `images/`
- Move `.sh` files to `scripts/`
- Display summary of organized files
- Handle errors gracefully

**Skills Practiced**:
- Directory creation
- File operations (move)
- Pattern matching
- Error handling

**Time Estimate**: 30-45 minutes

---

### Project 2: Directory Structure Creator
**Difficulty**: ⭐⭐ (Beginner)

**Description**: Create a script that sets up a standard project directory structure.

**Requirements**:
- Accept project name as input
- Create directory structure:
  ```
  project-name/
  ├── src/
  ├── docs/
  ├── tests/
  └── README.md
  ```
- Generate a basic README.md file
- Display created structure
- Add error handling

**Skills Practiced**:
- User input
- Directory creation
- File creation
- Output formatting

**Time Estimate**: 30-45 minutes

---

### Project 3: Basic Backup Script
**Difficulty**: ⭐⭐⭐ (Intermediate)

**Description**: Create a backup script that copies files to a timestamped backup directory.

**Requirements**:
- Accept source directory as input
- Create backup directory with timestamp
- Copy all files recursively
- Display backup location and size
- Handle errors (missing directory, permissions, etc.)

**Skills Practiced**:
- User input
- Date/time formatting
- File copying
- Error handling
- System information

**Time Estimate**: 45-60 minutes

## 🚀 Getting Started

1. **Read the project file**: Each project has a template with TODO comments
2. **Plan your solution**: Think about what commands you need
3. **Implement step by step**: Complete one requirement at a time
4. **Test thoroughly**: Test with different inputs and edge cases
5. **Refactor**: Clean up and improve your code

## ✅ Project Completion Checklist

For each project, ensure:
- [ ] Script has proper shebang line
- [ ] Script has comments explaining functionality
- [ ] All requirements are met
- [ ] Error handling is implemented
- [ ] Script is tested with various inputs
- [ ] Output is clear and helpful
- [ ] Code is readable and well-organized

## 💡 Tips

- **Start simple**: Get basic functionality working first
- **Test incrementally**: Test after each major feature
- **Handle errors**: Check if directories/files exist before operations
- **Use variables**: Make your code more maintainable
- **Add comments**: Explain complex logic
- **Test edge cases**: Empty directories, missing files, etc.

## 🎓 Bonus Challenges

After completing the basic projects, try these enhancements:

### File Organizer Enhancements:
- Add more file types (videos, archives, etc.)
- Preserve directory structure
- Add dry-run mode (show what would be done)
- Create log file of operations

### Directory Creator Enhancements:
- Add more directory types (config, logs, etc.)
- Generate .gitignore file
- Create initial files in subdirectories
- Support multiple project templates

### Backup Script Enhancements:
- Add compression (tar.gz)
- Keep multiple backup versions
- Exclude certain files/directories
- Add restore functionality
- Email notification on completion

## 📚 Next Steps

After completing all projects:
1. Review your code
2. Compare with solutions (if available)
3. Refactor for best practices
4. Document your learning
5. Move to the next module!
