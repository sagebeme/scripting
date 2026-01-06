# Level 6: Functions & Parsing

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Define and call functions
- Pass parameters to functions
- Return values from functions
- Use local variables
- Create recursive functions
- Parse command-line arguments
- Use getopts for option parsing
- Validate input effectively

## 📚 Topics Covered

### 1. Function Basics
- Function definition syntax
- Calling functions
- Function parameters
- Return values
- Exit codes from functions

### 2. Function Parameters
- Positional parameters in functions
- Passing arguments
- Accessing function arguments
- Default parameters

### 3. Local Variables
- Local variable scope
- Variable shadowing
- Global vs. local variables
- Best practices

### 4. Return Values
- Exit codes
- Returning data
- Capturing function output
- Error handling

### 5. Recursive Functions
- Recursion concepts
- Base cases
- Recursive examples
- When to use recursion

### 6. Command-Line Arguments
- Positional parameters ($1, $2, ...)
- $# - argument count
- $@ - all arguments
- $* - all arguments as string
- $0 - script name

### 7. getopts
- Option parsing
- Short options
- Option arguments
- Error handling
- Best practices

### 8. Input Validation
- Validate argument count
- Check file existence
- Validate data types
- Sanitize input
- Error messages

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Function Basics
- Define simple functions
- Call functions
- Pass parameters
- Return values

### Exercise 2: Advanced Functions
- Local variables
- Recursive functions
- Function libraries
- Scope management

### Exercise 3: Argument Parsing
- Handle positional parameters
- Process $@ and $*
- Validate argument count
- Process arguments

### Exercise 4: getopts
- Parse options with getopts
- Handle option arguments
- Error handling
- Combine with positional args

### Exercise 5: Input Validation
- Validate user input
- Check file paths
- Validate data types
- Sanitize input

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Modular Script Library
Create a library of reusable functions for common tasks.

### Project 2: CLI Tool with Options
Build a command-line tool with proper option parsing.

### Project 3: Argument Parser Utility
Create a utility that validates and parses arguments.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Function Basics (`examples/function-basics.sh`)
Demonstrate function definition and calling.

### Example 2: getopts Example (`examples/getopts-example.sh`)
Demonstrate option parsing with getopts.

## 🔍 Key Concepts

### Function Syntax
```bash
# Function definition
function_name() {
    commands
}

# Or
function function_name() {
    commands
}
```

### Returning Values
```bash
# Return exit code
return 0  # success
return 1  # failure

# Return data (via stdout)
echo "result"
```

### getopts Usage
```bash
while getopts "abc:" opt; do
    case $opt in
        a) echo "Option a" ;;
        b) echo "Option b" ;;
        c) echo "Option c with value: $OPTARG" ;;
        \?) echo "Invalid option" ;;
    esac
done
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Define and call functions
- [ ] Pass parameters to functions
- [ ] Use local variables
- [ ] Return values from functions
- [ ] Create recursive functions
- [ ] Parse command-line arguments
- [ ] Use getopts for options
- [ ] Validate input
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man bash` (see FUNCTIONS section)
- [Bash Functions](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html)
- [Advanced Bash Scripting Guide - Functions](https://tldp.org/LDP/abs/html/functions.html)

### Guides
- [Bash Functions Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php)
- [getopts Tutorial](https://www.mkssoftware.com/docs/man1/getopts.1.asp)
- [Command Line Arguments](https://www.gnu.org/software/bash/manual/html_node/Positional-Parameters.html)

### Tools
- [ShellCheck](https://www.shellcheck.net/) - Check function syntax
- [Bash Function Examples](https://www.commandlinefu.com/commands/browse)

### Practice
- [Bash Function Exercises](https://www.exercism.org/tracks/bash) - Practice problems
- [CLI Tool Design](https://clig.dev/) - Design better CLI tools

## 🎓 Next Steps

Once you've completed this module:
1. Practice creating function libraries
2. Build CLI tools with options
3. Master argument parsing
4. Move to **07-processes** module

---

**Remember**: Functions make code reusable and maintainable. Use them to organize your scripts!
