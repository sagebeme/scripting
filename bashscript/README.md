# Bash Scripting Mastery 🐚

> Learn shell scripting from basics to advanced automation and system administration.

## 📋 Course Overview

This track takes you from writing your first bash script to creating complex automation tools for system administration, deployment, and daily operations.

## 🎯 Learning Objectives

By completing this track, you will:
- Master shell commands and navigation
- Write efficient bash scripts
- Handle file permissions and ownership
- Use I/O redirections and filters effectively
- Work with variables and expansions
- Implement loops, conditions, and parsing
- Manage processes and signals
- Use regular expressions in scripts
- Build production-ready automation scripts

## 📚 Course Structure

### Level 1: Basics (01-basics)
**Duration: 1-2 weeks**

**Topics:**
- Introduction to shell and terminal
- Basic commands (ls, cd, pwd, mkdir, rm, cp, mv)
- File and directory operations
- Text editors (nano, vim basics)
- Writing your first script
- Shebang and script execution
- Comments and documentation

**Projects:**
- Simple file organizer script
- Directory structure creator
- Basic backup script

### Level 2: Permissions (02-permissions)
**Duration: 1 week**

**Topics:**
- Understanding file permissions (rwx)
- chmod, chown, chgrp commands
- Octal and symbolic notation
- SUID, SGID, and sticky bits
- umask and default permissions
- ACL (Access Control Lists)

**Projects:**
- Permission management script
- Secure file handler
- User permission checker

### Level 3: Redirections (03-redirections)
**Duration: 1 week**

**Topics:**
- Standard input, output, and error
- Redirection operators (>, >>, <, <<)
- Pipes and filters
- tee command
- Here documents
- Process substitution
- Combining commands

**Projects:**
- Log file processor
- Data transformation pipeline
- Error handling script

### Level 4: Variables & Expansions (04-variables)
**Duration: 1-2 weeks**

**Topics:**
- Variable assignment and usage
- Environment variables
- Parameter expansion
- Command substitution
- Arithmetic expansion
- Brace expansion
- Tilde expansion
- Pathname expansion (globbing)
- Quoting and escaping

**Projects:**
- Configuration file parser
- Dynamic script generator
- Environment setup script

### Level 5: Control Flow (05-control-flow)
**Duration: 2 weeks**

**Topics:**
- If/else statements
- Case statements
- For loops
- While and until loops
- Break and continue
- Nested loops
- Conditional operators (&&, ||)
- Test command and [ ]

**Projects:**
- Menu-driven script
- File processor with conditions
- Interactive configuration tool

### Level 6: Functions & Parsing (06-functions)
**Duration: 1-2 weeks**

**Topics:**
- Function definition and calling
- Function parameters
- Return values
- Local variables
- Recursive functions
- Command-line argument parsing
- getopts for option parsing
- Input validation

**Projects:**
- Modular script library
- CLI tool with options
- Argument parser utility

### Level 7: Processes & Signals (07-processes)
**Duration: 1-2 weeks**

**Topics:**
- Process management
- Background processes
- Job control (fg, bg, jobs)
- Process substitution
- Signal handling (trap)
- Process monitoring
- Process communication
- Exit codes and error handling

**Projects:**
- Process monitor script
- Signal handler utility
- Background task manager

### Level 8: Regular Expressions (08-regex)
**Duration: 1-2 weeks**

**Topics:**
- Basic regex patterns
- Character classes
- Quantifiers
- Anchors and boundaries
- Groups and backreferences
- grep, sed, awk basics
- Pattern matching in bash
- Advanced text processing

**Projects:**
- Log analyzer
- Text parser and formatter
- Data extraction tool

### Level 9: Advanced Scripting (09-advanced)
**Duration: 2-3 weeks**

**Topics:**
- Arrays and associative arrays
- String manipulation
- File I/O operations
- Error handling best practices
- Debugging techniques (set -x, -e, -u)
- Script optimization
- Security considerations
- Best practices and style guides

**Projects:**
- System monitoring dashboard
- Automated deployment script
- Configuration management tool

### Level 10: Real-World Projects (10-projects)
**Duration: 2-3 weeks**

**Capstone Projects:**
- Automated backup system
- System health monitor
- Log rotation and cleanup

**Practice Exercises:**
- Backup practice exercises
- Monitoring practice exercises
- Log rotation practice exercises
- Integration practice exercises

**Examples:**
- Backup system examples
- System monitoring examples
- Log rotation examples

## 🚀 Getting Started

1. **Prerequisites:**
   - Linux/Unix system or WSL (Windows Subsystem for Linux)
   - Basic familiarity with command line
   - Text editor (vim, nano, or VS Code)

2. **Setup:**
   ```bash
   # Verify bash version
   bash --version
   
   # Make scripts executable
   chmod +x script.sh
   
   # Run scripts
   ./script.sh
   # or
   bash script.sh
   ```

3. **Learning Path:**
   - Start with `01-basics/`
   - Complete each module in order
   - Read the README in each module
   - Complete all exercises
   - Build the projects
   - Move to next module

## 📖 Module Structure

Each module contains:
```
module-name/
├── README.md          # Learning objectives and topics
├── examples/          # Example scripts
├── exercises/         # Practice exercises
├── projects/          # Project assignments
└── solutions/         # Reference solutions (optional)
```

## 💡 Learning Tips

1. **Practice Daily**: Write scripts every day, even small ones
2. **Read Documentation**: Use `man` pages and `--help` flags
3. **Test Thoroughly**: Test scripts with different inputs
4. **Debug Systematically**: Use `set -x` to trace execution
5. **Follow Best Practices**: Write readable, maintainable code
6. **Version Control**: Commit your scripts to git
7. **Review Code**: Read other people's scripts
8. **Build Projects**: Apply what you learn in real projects

## 🔧 Essential Commands Reference

```bash
# File operations
ls, cd, pwd, mkdir, rm, cp, mv, cat, less, head, tail

# Text processing
grep, sed, awk, cut, sort, uniq, wc, tr

# System info
ps, top, df, du, free, uname, whoami

# Permissions
chmod, chown, chgrp, umask

# Process management
jobs, fg, bg, kill, killall, nohup

# Network
ping, curl, wget, netstat, ss
```

## 📚 Additional Resources

### Official Documentation
- [Bash Manual](https://www.gnu.org/software/bash/manual/) - Official GNU Bash manual
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) - Complete reference
- `man bash` - Local manual pages (run in terminal)

### Beginner Guides
- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/) - Comprehensive beginner guide
- [Linux Command Line Basics](https://linuxcommand.org/) - Learn command line fundamentals
- [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/) - Interactive tutorial

### Advanced Guides
- [Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/) - Advanced concepts and techniques
- [Bash Best Practices](https://mywiki.wooledge.org/BashGuide) - Best practices and pitfalls
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) - Code style guide

### Tools & Utilities
- [ShellCheck](https://www.shellcheck.net/) - Online bash linter and static analysis
- [Explain Shell](https://explainshell.com/) - Explains shell commands
- [Bash Hackers Wiki](https://wiki.bash-hackers.org/) - Bash scripting wiki

### Practice & Learning
- [Bash Academy](https://www.bash.academy/) - Interactive bash learning
- [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) - Security-focused bash practice
- [HackerRank Shell](https://www.hackerrank.com/domains/shell) - Practice problems

### Cheat Sheets
- [Bash Cheat Sheet](https://devhints.io/bash) - Quick reference
- [Bash One-Liners](https://www.commandlinefu.com/) - Useful one-liners
- [Linux Command Cheat Sheet](https://www.guru99.com/linux-commands-cheat-sheet.html)

### Video Tutorials
- [Bash Scripting Playlist](https://www.youtube.com/results?search_query=bash+scripting+tutorial) - YouTube tutorials
- [Linux Academy Bash Course](https://linuxacademy.com/) - Comprehensive courses

### Community & Forums
- [Stack Overflow - Bash Tag](https://stackoverflow.com/questions/tagged/bash)
- [Reddit r/bash](https://www.reddit.com/r/bash/) - Bash community
- [Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/tagged/bash)

## ✅ Progress Checklist

- [ ] Level 1: Basics
- [ ] Level 2: Permissions
- [ ] Level 3: Redirections
- [ ] Level 4: Variables & Expansions
- [ ] Level 5: Control Flow
- [ ] Level 6: Functions & Parsing
- [ ] Level 7: Processes & Signals
- [ ] Level 8: Regular Expressions
- [ ] Level 9: Advanced Scripting
- [ ] Level 10: Real-World Projects

## 🎓 Certification Path

After completing all modules:
1. Complete all exercises
2. Build all projects
3. Create a portfolio of 3-5 original scripts
4. Document your learning journey
5. Share your work on GitHub

---

**Ready to start? Begin with `01-basics/` and work your way through each module!**

*Remember: Mastery comes from practice. Write scripts, break them, fix them, and learn!*
