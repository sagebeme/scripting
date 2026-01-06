# Level 1: Bash Scripting Basics

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Navigate the Linux file system using command line
- Use basic shell commands effectively
- Write and execute your first bash script
- Understand shebang and script permissions
- Use text editors for script creation
- Add comments and documentation to scripts

## 📚 Topics Covered

### 1. Introduction to Shell
- What is a shell?
- Different shell types (bash, zsh, sh)
- Terminal vs. shell
- Opening a terminal

### 2. Basic Commands
- `pwd` - Print working directory
- `ls` - List directory contents
- `cd` - Change directory
- `mkdir` - Create directories
- `rm` - Remove files/directories
- `cp` - Copy files
- `mv` - Move/rename files
- `cat` - Display file contents
- `touch` - Create empty files

### 3. File System Navigation
- Absolute vs. relative paths
- Home directory (`~`)
- Parent directory (`..`)
- Current directory (`.`)
- Path expansion

### 4. Text Editors
- **nano**: Beginner-friendly editor
- **vim**: Advanced editor (basics)
- **VS Code**: GUI editor
- Creating and editing files

### 5. Writing Your First Script
- What is a script?
- Creating a script file
- Making scripts executable (`chmod +x`)
- Running scripts (`./script.sh` or `bash script.sh`)

### 6. Shebang Line
- What is shebang (`#!/bin/bash`)?
- Why it's important
- Different shebang options
- Finding bash path (`which bash`)

### 7. Comments and Documentation
- Single-line comments (`#`)
- Multi-line comments
- Documenting your code
- Best practices

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Basic Navigation (`exercises/exercise-1-navigation.sh`)
Practice navigating the file system:
- Navigate directories
- Create directories
- List directory contents
- Use pwd command

### Exercise 2: File Operations (`exercises/exercise-2-file-operations.sh`)
Learn file creation, copying, moving, and deletion:
- Create files
- Add content to files
- Copy files
- Rename files
- Delete files

### Exercise 3: Your First Script (`exercises/exercise-3-first-script.sh`)
Write a complete working script:
- Add shebang
- Add comments
- Use echo command
- Display system information

### Exercise 4: Practice with Commands (`exercises/exercise-4-commands.sh`)
Combine multiple commands:
- Create directories and files
- Copy and move files
- Remove files and directories
- Practice command chaining

**Instructions**: 
1. Open each exercise file
2. Read the comments and add the appropriate commands
3. Make executable: `chmod +x exercise-name.sh`
4. Run: `./exercise-name.sh`
5. See [`exercises/README.md`](./exercises/README.md) for detailed instructions

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates and detailed requirements.

### Project 1: Simple File Organizer (`projects/project-1-file-organizer.sh`)
Create a script that:
- Creates three directories: `documents`, `images`, `scripts`
- Moves `.txt` files to `documents`
- Moves `.jpg`, `.png` files to `images`
- Moves `.sh` files to `scripts`
- Displays a summary of organized files

**Requirements:**
- Use proper shebang
- Add comments explaining each step
- Handle errors gracefully
- Display helpful messages

### Project 2: Directory Structure Creator (`projects/project-2-directory-creator.sh`)
Create a script that:
- Takes a project name as input
- Creates a directory structure:
  ```
  project-name/
  ├── src/
  ├── docs/
  ├── tests/
  └── README.md
  ```
- Creates a basic README.md file
- Displays the created structure

### Project 3: Basic Backup Script (`projects/project-3-backup-script.sh`)
Create a script that:
- Takes a source directory as input
- Creates a backup directory with timestamp
- Copies all files from source to backup
- Displays backup location and size
- Shows completion message

**Instructions**: 
1. Open each project file (they have TODO comments)
2. Complete the requirements
3. Test thoroughly
4. See [`projects/README.md`](./projects/README.md) for detailed requirements and tips

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working example scripts you can run and study.

### Example 1: Hello World (`examples/hello-world.sh`)
Simple hello world script demonstrating basic echo command.

### Example 2: System Information (`examples/system-info.sh`)
Display basic system information using command substitution.

### Example 3: Directory Lister (`examples/directory-lister.sh`)
List files in current directory with details and count.

### Example 4: File Creator (`examples/file-creator.sh`)
Create a file with content and display it.

**Instructions**: 
1. Navigate to the `examples/` directory
2. Make scripts executable: `chmod +x example-name.sh`
3. Run: `./example-name.sh`
4. Study the code to understand how it works

## 🔍 Key Concepts

### Shebang Explained
```bash
#!/bin/bash
```
- `#!` tells the system which interpreter to use
- `/bin/bash` is the path to the bash interpreter
- Must be the first line of the script
- No spaces allowed after `#!`

### Making Scripts Executable
```bash
# Method 1: Using chmod
chmod +x script.sh
./script.sh

# Method 2: Direct execution
bash script.sh
sh script.sh
```

### Comments
```bash
# Single-line comment

# Multi-line comments
# are just multiple
# single-line comments

# Or use here-document for documentation
: <<'COMMENT'
This is a multi-line comment block
that won't be executed
COMMENT
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Navigate the file system using command line
- [ ] Create, copy, move, and delete files/directories
- [ ] Use a text editor to create scripts
- [ ] Write a script with proper shebang
- [ ] Make scripts executable
- [ ] Run scripts successfully
- [ ] Add comments to your code
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man bash` - Bash manual
- `man ls`, `man cd`, `man mkdir` - Command manuals
- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/)

### Learning
- [Linux Command Line Basics](https://linuxcommand.org/) - Interactive tutorial
- [Learn Shell](https://www.learnshell.org/) - Interactive shell tutorial
- [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/)

### Tools
- [Explain Shell](https://explainshell.com/) - Understand shell commands
- [ShellCheck](https://www.shellcheck.net/) - Lint your scripts

### Practice
- [Command Line Challenge](https://cmdchallenge.com/) - Practice commands
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) - Security practice

## 🎓 Next Steps

Once you've completed this module:
1. Review your scripts
2. Test edge cases
3. Refactor for clarity
4. Move to **02-permissions** module

---

**Remember**: Practice makes perfect! Write scripts daily and experiment with different commands.
