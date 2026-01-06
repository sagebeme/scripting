# Projects - Level 2: Permissions

## 🎯 Project Overview

These projects will help you apply permission management skills in real-world scenarios.

## 📋 Project List

### Project 1: Permission Management Script
**Difficulty**: ⭐⭐⭐ (Intermediate)

**Description**: Create a script that analyzes file permissions and identifies security issues.

**Requirements**:
- Analyze permissions in a directory
- Identify insecure permissions (world-writable, etc.)
- Suggest appropriate fixes
- Generate a security report
- Optionally apply fixes with confirmation

**Skills Practiced**:
- Permission analysis
- Security assessment
- File permission manipulation
- Report generation

**Time Estimate**: 45-60 minutes

---

### Project 2: Secure File Handler
**Difficulty**: ⭐⭐ (Beginner-Intermediate)

**Description**: Create a script that handles file creation with secure default permissions.

**Requirements**:
- Set secure umask
- Create files with appropriate permissions
- Handle different file types (sensitive, scripts, regular)
- Verify permissions
- Restore original umask

**Skills Practiced**:
- umask configuration
- Secure file creation
- Permission setting
- Function creation

**Time Estimate**: 30-45 minutes

---

### Project 3: User Permission Checker
**Difficulty**: ⭐⭐⭐ (Intermediate)

**Description**: Create a script that checks what permissions a user has on files.

**Requirements**:
- Check file ownership
- Verify group membership
- Determine effective permissions
- Test actual access (read/write/execute)
- Generate detailed report

**Skills Practiced**:
- Permission analysis
- User/group checking
- Access testing
- Report generation

**Time Estimate**: 45-60 minutes

## 🚀 Getting Started

1. **Read the project file**: Each project has a template with TODO comments
2. **Plan your solution**: Think about what commands you need
3. **Implement step by step**: Complete one requirement at a time
4. **Test thoroughly**: Test with different files and users
5. **Refactor**: Clean up and improve your code

## ✅ Project Completion Checklist

For each project, ensure:
- [ ] Script has proper shebang and comments
- [ ] All requirements are met
- [ ] Error handling is implemented
- [ ] Script is tested with various scenarios
- [ ] Output is clear and helpful
- [ ] Security considerations are addressed
- [ ] Code is readable and well-organized

## 💡 Tips

- **Security first**: Always consider security implications
- **Test with different users**: Use sudo to test ownership scenarios
- **Handle errors**: Check if files exist, if user has permissions, etc.
- **Use functions**: Break complex logic into functions
- **Validate input**: Check user input before processing
- **Document**: Add comments explaining security decisions

## 🎓 Bonus Challenges

After completing the basic projects, try these enhancements:

### Permission Manager Enhancements:
- Recursive directory analysis
- Fix insecure permissions automatically
- Generate HTML report
- Email alerts for critical issues
- Log all changes

### Secure File Handler Enhancements:
- Support for multiple file types
- Configuration file for permission templates
- Backup original permissions
- Restore functionality
- Batch file processing

### Permission Checker Enhancements:
- Check multiple files/directories
- Compare permissions across files
- Find files user can/cannot access
- Generate permission matrix
- Export to CSV/JSON

## 📚 Next Steps

After completing all projects:
1. Review your code
2. Test with different scenarios
3. Understand security implications
4. Move to the next module!
