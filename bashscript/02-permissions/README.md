# Level 2: Permissions

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Understand Linux file permissions (read, write, execute)
- Use chmod to change file permissions
- Work with octal and symbolic notation
- Manage file ownership (chown, chgrp)
- Understand SUID, SGID, and sticky bits
- Configure umask for default permissions
- Work with Access Control Lists (ACL)
- Secure files and directories appropriately

## 📚 Topics Covered

### 1. Understanding File Permissions
- What are permissions?
- Three permission types: read (r), write (w), execute (x)
- Three user categories: owner, group, others
- Permission representation (rwxrwxrwx)
- Viewing permissions with `ls -l`

### 2. chmod Command
- Changing permissions with chmod
- Symbolic notation (u, g, o, a)
- Adding permissions (+)
- Removing permissions (-)
- Setting permissions (=)
- Examples and practice

### 3. Octal Notation
- Understanding octal numbers (0-7)
- Permission to octal conversion
- Common permission values
- Using chmod with octal notation
- Quick reference guide

### 4. File Ownership
- Understanding ownership (user and group)
- chown command
- chgrp command
- Changing ownership recursively
- Preserving ownership when copying

### 5. Special Permissions
- SUID (Set User ID)
- SGID (Set Group ID)
- Sticky bit
- When to use special permissions
- Security implications

### 6. umask
- What is umask?
- Default permissions calculation
- Setting umask values
- System-wide vs. user umask
- Common umask values

### 7. Access Control Lists (ACL)
- What are ACLs?
- When to use ACLs
- getfacl and setfacl commands
- Setting ACL permissions
- Default ACLs

### 8. Permission Best Practices
- Principle of least privilege
- Securing scripts
- Securing directories
- Common permission mistakes
- Security considerations

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Viewing Permissions
- List files with detailed permissions
- Understand permission notation
- Identify file types

### Exercise 2: Changing Permissions with chmod
- Use symbolic notation
- Use octal notation
- Practice common permission changes

### Exercise 3: File Ownership
- Change file ownership
- Change group ownership
- Work with ownership recursively

### Exercise 4: Special Permissions
- Set SUID on files
- Set SGID on directories
- Set sticky bit
- Understand when to use each

### Exercise 5: umask Practice
- Set umask values
- Create files and directories
- Verify default permissions

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Permission Management Script
Create a script that:
- Analyzes file permissions in a directory
- Reports files with insecure permissions
- Suggests permission fixes
- Applies secure permissions

### Project 2: Secure File Handler
Create a script that:
- Creates files with secure default permissions
- Protects sensitive files (600)
- Makes scripts executable (755)
- Handles directory permissions

### Project 3: User Permission Checker
Create a script that:
- Checks user permissions on files
- Verifies group membership
- Reports access rights
- Tests read/write/execute permissions

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Permission Viewer
Display detailed permission information for files.

### Example 2: Permission Setter
Safely set permissions using different methods.

### Example 3: Ownership Manager
Change ownership with validation.

## 🔍 Key Concepts

### Permission Notation
```
-rwxrwxrwx
│└─┴─┴─┴─┴─┴─┴─┴─┴─┴─
│ │ │ │ │ │ │ │ │ │
│ │ │ │ │ │ │ │ │ └─ Others: execute
│ │ │ │ │ │ │ │ └── Others: write
│ │ │ │ │ │ │ └──── Others: read
│ │ │ │ │ │ └────── Group: execute
│ │ │ │ │ └──────── Group: write
│ │ │ │ └────────── Group: read
│ │ │ └──────────── Owner: execute
│ │ └────────────── Owner: write
│ └──────────────── Owner: read
└────────────────── File type (- = file, d = directory)
```

### Common Permission Values
- `755`: rwxr-xr-x (scripts, executables)
- `644`: rw-r--r-- (regular files)
- `600`: rw------- (private files)
- `700`: rwx------ (private directories)
- `750`: rwxr-x--- (group-accessible)

### Octal to Permission
```
7 = rwx (read + write + execute)
6 = rw- (read + write)
5 = r-x (read + execute)
4 = r-- (read only)
3 = -wx (write + execute)
2 = -w- (write only)
1 = --x (execute only)
0 = --- (no permissions)
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Understand permission notation (rwx)
- [ ] Use chmod with symbolic notation
- [ ] Use chmod with octal notation
- [ ] Change file ownership (chown)
- [ ] Change group ownership (chgrp)
- [ ] Understand and use SUID, SGID, sticky bit
- [ ] Configure umask
- [ ] Work with ACLs (basic)
- [ ] Apply security best practices
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man chmod` - Change file permissions
- `man chown` - Change file ownership
- `man umask` - Set default permissions
- `man getfacl`, `man setfacl` - ACL commands

### Guides
- [Linux File Permissions Guide](https://www.linux.com/training-tutorials/understanding-linux-file-permissions/)
- [Understanding Linux Permissions](https://www.linuxfoundation.org/blog/classic-sysadmin-understanding-linux-file-permissions/)
- [File Permissions Explained](https://www.guru99.com/file-permissions.html)

### Tools
- [chmod Calculator](https://chmod-calculator.com/) - Calculate permission values
- [File Permission Visualizer](https://chmodcommand.com/) - Visual permission tool

### Security
- [Linux Security Best Practices](https://www.cyberciti.biz/tips/linux-security.html)
- [Principle of Least Privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different permission scenarios
2. Secure your own scripts
3. Understand security implications
4. Move to **03-redirections** module

---

**Remember**: Permissions are crucial for security. Always follow the principle of least privilege!
