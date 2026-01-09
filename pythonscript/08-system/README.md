# Level 8: System & OS Operations

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Interact with the operating system
- Work with environment variables
- Handle command-line arguments
- Execute system commands
- Manage processes
- Work with file systems
- Get system information
- Write cross-platform scripts

## 📚 Topics Covered

### 1. os Module
- os.getcwd()
- os.chdir()
- os.listdir()
- os.makedirs()
- os.remove()
- os.path operations
- os.environ

### 2. sys Module
- sys.argv
- sys.path
- sys.exit()
- sys.stdin/stdout/stderr
- sys.platform

### 3. Environment Variables
- Reading environment variables
- Setting environment variables
- .env files
- python-dotenv

### 4. Command-Line Arguments
- sys.argv
- argparse module
- Positional arguments
- Optional arguments
- Subcommands
- Help messages

### 5. subprocess Module
- subprocess.run()
- subprocess.Popen()
- Capturing output
- Running shell commands
- Process communication
- Error handling

### 6. Process Management
- Process creation
- Process monitoring
- Process termination
- Process communication
- Background processes

### 7. File System Operations
- Path operations
- Directory traversal
- File permissions
- Symbolic links
- File metadata

### 8. System Information
- Platform detection
- System resources
- CPU and memory info
- Disk usage
- Network interfaces

### 9. Cross-Platform Compatibility
- Platform-specific code
- Path separators
- Line endings
- File permissions
- Testing on multiple platforms

### 10. Best Practices
- Security considerations
- Error handling
- Resource cleanup
- Performance optimization

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: os Module
- Navigate directories
- List files
- Create/remove directories

### Exercise 2: Command-Line Arguments
- Parse arguments with argparse
- Handle different argument types
- Create CLI interfaces

### Exercise 3: subprocess
- Run system commands
- Capture output
- Handle errors

### Exercise 4: Environment Variables
- Read/write environment variables
- Use .env files
- Manage configuration

### Exercise 5: System Information
- Get platform info
- Check system resources
- Monitor processes

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: System Information Script
Display system information.

### Project 2: Process Monitor
Monitor running processes.

### Project 3: Automated Backup Tool
Create backup automation.

### Project 4: File Synchronizer
Synchronize files between directories.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: os Operations
Demonstrate OS interactions.

### Example 2: argparse
Show command-line parsing.

### Example 3: subprocess
Demonstrate process execution.

## 🔍 Key Concepts

### Command-Line Arguments
```python
import argparse

parser = argparse.ArgumentParser(description='My script')
parser.add_argument('input', help='Input file')
parser.add_argument('-o', '--output', help='Output file')
args = parser.parse_args()
```

### subprocess
```python
import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

### Environment Variables
```python
import os

value = os.environ.get('MY_VAR', 'default')
os.environ['MY_VAR'] = 'new_value'
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Use os and sys modules
- [ ] Work with environment variables
- [ ] Parse command-line arguments
- [ ] Execute system commands
- [ ] Manage processes
- [ ] Get system information
- [ ] Write cross-platform code
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [os module](https://docs.python.org/3/library/os.html)
- [sys module](https://docs.python.org/3/library/sys.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)

### Learning
- [Real Python - System Operations](https://realpython.com/python-subprocess/)
- [Command-Line Interfaces](https://realpython.com/command-line-interfaces-python-argparse/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice system operations
2. Master argparse
3. Build automation scripts
4. Move to **09-networking** module

---

**Remember**: Be careful with system operations. Always validate input and handle errors!
