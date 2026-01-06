# Level 7: Processes & Signals

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Manage processes effectively
- Run commands in background
- Use job control (fg, bg, jobs)
- Handle signals with trap
- Monitor processes
- Understand process communication
- Handle exit codes properly
- Use process substitution

## 📚 Topics Covered

### 1. Process Management
- What is a process?
- Process IDs (PID)
- Parent and child processes
- Process hierarchy
- Viewing processes (ps, top)

### 2. Background Processes
- Running commands in background (&)
- nohup command
- Disown command
- Background process management

### 3. Job Control
- jobs command
- fg (foreground)
- bg (background)
- Job numbers
- Job control signals

### 4. Signal Handling
- What are signals?
- Common signals (SIGINT, SIGTERM, SIGHUP, etc.)
- trap command
- Signal handlers
- Ignoring signals

### 5. Process Substitution
- <() input process substitution
- >() output process substitution
- When to use process substitution
- Practical examples

### 6. Process Monitoring
- Check if process is running
- Monitor process status
- Process resource usage
- Process tree

### 7. Exit Codes
- Understanding exit codes
- Setting exit codes
- Checking command success
- Error handling with exit codes

### 8. Process Communication
- Pipes for communication
- Named pipes (FIFO)
- Process synchronization
- Inter-process communication

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Process Management
- View running processes
- Find process IDs
- Check process status

### Exercise 2: Background Processes
- Run commands in background
- Use nohup
- Manage background jobs

### Exercise 3: Signal Handling
- Use trap command
- Handle SIGINT
- Handle SIGTERM
- Custom signal handlers

### Exercise 4: Exit Codes
- Check exit codes
- Set exit codes
- Handle command failures

### Exercise 5: Process Monitoring
- Monitor process status
- Check if process is running
- Process resource monitoring

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Process Monitor Script
Create a script that monitors processes and reports status.

### Project 2: Signal Handler Utility
Create a utility that handles signals gracefully.

### Project 3: Background Task Manager
Create a script that manages background tasks.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Background Processes (`examples/background-processes.sh`)
Demonstrate running commands in background.

### Example 2: Signal Handling (`examples/signal-handling.sh`)
Show how to handle signals with trap.

## 🔍 Key Concepts

### Background Processes
```bash
# Run in background
command &

# Run with nohup
nohup command &

# Disown process
command &
disown
```

### Signal Handling
```bash
# Trap SIGINT (Ctrl+C)
trap 'cleanup; exit' INT

# Trap multiple signals
trap 'cleanup' INT TERM EXIT

# Ignore signal
trap '' INT
```

### Exit Codes
```bash
# Check exit code
command
if [ $? -eq 0 ]; then
    echo "Success"
fi

# Set exit code
exit 0  # success
exit 1  # failure
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Manage processes
- [ ] Run commands in background
- [ ] Use job control
- [ ] Handle signals with trap
- [ ] Monitor processes
- [ ] Understand exit codes
- [ ] Use process substitution
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man bash` (see JOB CONTROL and SIGNALS sections)
- `man trap` - Signal handling
- `man jobs`, `man fg`, `man bg` - Job control
- `man nohup` - Run commands immune to hangups
- `man ps`, `man top` - Process management

### Guides
- [Bash Job Control](https://www.gnu.org/software/bash/manual/html_node/Job-Control.html)
- [Signal Handling Guide](https://www.gnu.org/software/bash/manual/html_node/Signals.html)
- [Process Management Tutorial](https://www.tldp.org/LDP/abs/html/process-management.html)

### Tools
- `htop` - Interactive process viewer
- `pgrep`, `pkill` - Process utilities
- [Process Monitoring Tools](https://www.tecmint.com/linux-process-management/)

### Practice
- [Process Management Exercises](https://www.exercism.org/tracks/bash)
- [System Administration Practice](https://www.linuxacademy.com/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice process management
2. Build monitoring scripts
3. Master signal handling
4. Move to **08-regex** module

---

**Remember**: Process management is crucial for system administration. Master it!
