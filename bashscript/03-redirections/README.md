# Level 3: Redirections

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Understand standard input, output, and error streams
- Use redirection operators (>, >>, <, <<)
- Combine commands with pipes (|)
- Use filters effectively
- Work with the tee command
- Create here documents
- Use process substitution
- Combine multiple commands effectively

## 📚 Topics Covered

### 1. Standard Streams
- Standard Input (stdin) - file descriptor 0
- Standard Output (stdout) - file descriptor 1
- Standard Error (stderr) - file descriptor 2
- Understanding file descriptors
- Redirecting each stream

### 2. Output Redirection
- `>` - Redirect output (overwrite)
- `>>` - Redirect output (append)
- Redirecting stdout
- Redirecting stderr (`2>`)
- Redirecting both (`&>` or `2>&1`)
- Appending errors (`2>>`)

### 3. Input Redirection
- `<` - Redirect input from file
- Reading from files
- Combining input and output redirection
- Practical examples

### 4. Here Documents
- `<<` - Here document operator
- Creating multi-line input
- Using here documents in scripts
- Here strings (`<<<`)
- Practical applications

### 5. Pipes
- `|` - Pipe operator
- Connecting command output to input
- Chaining multiple commands
- Common pipe patterns
- Performance considerations

### 6. Filters
- Common filter commands:
  - `grep` - Search patterns
  - `sort` - Sort lines
  - `uniq` - Remove duplicates
  - `cut` - Extract columns
  - `awk` - Text processing
  - `sed` - Stream editor
  - `head` - First lines
  - `tail` - Last lines
  - `wc` - Word count
  - `tr` - Translate characters

### 7. tee Command
- What is tee?
- Writing to file and stdout
- Appending with tee -a
- Using tee in pipelines
- Practical examples

### 8. Process Substitution
- `<()` - Input process substitution
- `>()` - Output process substitution
- When to use process substitution
- Advanced examples

### 9. Combining Commands
- Command chaining with `;`
- Conditional execution with `&&` and `||`
- Combining with pipes and redirections
- Complex command combinations

### 10. Error Handling
- Redirecting errors
- Discarding output (`/dev/null`)
- Error logging
- Best practices

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Basic Redirections
- Redirect output to files
- Append to files
- Redirect errors
- Combine stdout and stderr

### Exercise 2: Input Redirection
- Read from files
- Use here documents
- Combine input/output redirection

### Exercise 3: Pipes and Filters
- Chain commands with pipes
- Use grep, sort, uniq
- Combine multiple filters
- Process data pipelines

### Exercise 4: Advanced Redirections
- Use tee command
- Process substitution
- Complex redirections
- Error handling

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Log File Processor
Create a script that:
- Reads log files
- Filters and processes log entries
- Generates reports
- Handles errors appropriately

### Project 2: Data Transformation Pipeline
Create a script that:
- Reads data from files
- Transforms data using filters
- Outputs to multiple formats
- Uses pipes effectively

### Project 3: Error Handling Script
Create a script that:
- Captures both output and errors
- Logs errors to files
- Displays success messages
- Handles different error scenarios

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Basic Redirections
Demonstrate output and input redirection.

### Example 2: Pipe Examples
Show various pipe patterns and filters.

### Example 3: Here Document
Create scripts using here documents.

## 🔍 Key Concepts

### Redirection Operators
```bash
# Output redirection
command > file          # Overwrite file
command >> file         # Append to file
command 2> file         # Redirect errors
command &> file         # Redirect both
command 2>&1            # Redirect stderr to stdout

# Input redirection
command < file          # Read from file
command << EOF          # Here document
command <<< "string"    # Here string

# Pipes
command1 | command2     # Pipe output
command1 | tee file     # Save and display
```

### Common Filter Patterns
```bash
# Search and filter
grep "pattern" file
grep -v "pattern" file  # Invert match

# Sort and unique
sort file | uniq
sort -u file            # Sort and unique

# Extract columns
cut -d: -f1 file
awk '{print $1}' file

# Count lines
wc -l file
grep "pattern" file | wc -l
```

### Combining Commands
```bash
# Sequential execution
cmd1; cmd2; cmd3

# Conditional execution
cmd1 && cmd2            # Run cmd2 if cmd1 succeeds
cmd1 || cmd2            # Run cmd2 if cmd1 fails

# Complex combinations
cmd1 | cmd2 && cmd3 || cmd4
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Understand stdin, stdout, stderr
- [ ] Use output redirection (>, >>)
- [ ] Use input redirection (<)
- [ ] Redirect errors (2>, &>)
- [ ] Use here documents (<<)
- [ ] Chain commands with pipes (|)
- [ ] Use common filters (grep, sort, etc.)
- [ ] Use tee command
- [ ] Combine multiple redirections
- [ ] Handle errors appropriately
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man bash` (see REDIRECTION section)
- `man grep` - Pattern searching
- `man sed` - Stream editor
- `man awk` - Text processing
- `man sort`, `man uniq`, `man cut` - Text utilities

### Guides
- [Bash Redirections Guide](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
- [I/O Redirection Tutorial](https://www.tldp.org/LDP/abs/html/io-redirection.html)
- [Pipes and Filters](https://swcarpentry.github.io/shell-novice/04-pipefilter.html)

### Tools
- [Explain Shell](https://explainshell.com/) - Understand complex commands
- [Regex101](https://regex101.com/) - Test regex patterns

### Practice
- [Command Line Challenge](https://cmdchallenge.com/) - Practice pipelines
- [Bash One-Liners](https://www.commandlinefu.com/) - Useful examples

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different data sources
2. Build data processing pipelines
3. Optimize command combinations
4. Move to **04-variables** module

---

**Remember**: Redirections and pipes are powerful tools for data processing. Master them to become efficient!
