# Exercises - Level 2: Permissions

## 📝 How to Complete Exercises

1. **Read the exercise file**: Each exercise has comments explaining what to do
2. **Add your commands**: Replace comments with actual bash commands
3. **Make executable**: Run `chmod +x exercise-name.sh`
4. **Test your solution**: Run `./exercise-name.sh`
5. **Compare with solutions**: Check the `solutions/` directory (after attempting)

## 📋 Exercise List

### Exercise 1: Viewing Permissions (`exercise-1-viewing-permissions.sh`)
**Objective**: Learn to view and interpret file permissions
- List files with detailed permissions
- Understand permission notation
- Identify file types
- Extract permission information

**Time**: 15-20 minutes

### Exercise 2: Changing Permissions with chmod (`exercise-2-chmod.sh`)
**Objective**: Master the chmod command
- Use symbolic notation (u, g, o, +, -, =)
- Use octal notation (755, 644, etc.)
- Change file and directory permissions
- Verify permission changes

**Time**: 20-25 minutes

### Exercise 3: File Ownership (`exercise-3-ownership.sh`)
**Objective**: Work with file ownership
- View current ownership
- Change file ownership (chown)
- Change group ownership (chgrp)
- Work with ownership recursively
- Understand user and group IDs

**Time**: 15-20 minutes
**Note**: Some commands may require sudo

### Exercise 4: Special Permissions (`exercise-4-special-permissions.sh`)
**Objective**: Understand and use special permissions
- Set SUID (Set User ID)
- Set SGID (Set Group ID)
- Set sticky bit
- Understand security implications
- Remove special permissions

**Time**: 20-25 minutes
**Note**: Some commands may require sudo

### Exercise 5: umask Practice (`exercise-5-umask.sh`)
**Objective**: Configure default permissions
- View current umask
- Set umask values
- Calculate resulting permissions
- Understand umask calculation
- Apply different umask values

**Time**: 15-20 minutes

## ✅ Completion Checklist

Before moving on, ensure you can:
- [ ] View and interpret file permissions
- [ ] Use chmod with both symbolic and octal notation
- [ ] Change file and directory ownership
- [ ] Understand and use special permissions
- [ ] Configure and use umask
- [ ] Calculate permissions from umask
- [ ] Complete all exercises without looking at solutions first

## 💡 Tips

- **Practice both notations**: Learn symbolic and octal
- **Understand the math**: Know how umask calculates permissions
- **Security first**: Always consider security implications
- **Use man pages**: `man chmod`, `man chown`, `man umask`
- **Test permissions**: Verify changes after modifying permissions

## 🚀 Next Steps

After completing all exercises:
1. Review your solutions
2. Practice with different scenarios
3. Understand security implications
4. Move to the Projects section
