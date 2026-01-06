# Level 4: Variables & Expansions

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Create and use variables in bash
- Understand variable scope
- Work with environment variables
- Use parameter expansion
- Perform command substitution
- Use arithmetic expansion
- Understand brace expansion
- Work with pathname expansion (globbing)
- Properly quote variables
- Escape special characters

## 📚 Topics Covered

### 1. Variable Basics
- Variable assignment
- Variable naming rules
- Accessing variables ($VAR or ${VAR})
- Unsetting variables (unset)
- Variable types (strings, integers)
- Variable scope (local vs. global)

### 2. Environment Variables
- What are environment variables?
- Viewing environment variables (env, printenv)
- Setting environment variables (export)
- Common environment variables:
  - PATH, HOME, USER, SHELL
  - PWD, OLDPWD
  - PS1, PS2
- Persistent environment variables

### 3. Parameter Expansion
- Basic expansion: ${variable}
- Default values: ${var:-default}
- Assign default: ${var:=default}
- Error if unset: ${var:?message}
- Use alternate: ${var:+value}
- String length: ${#var}
- Substring: ${var:offset:length}
- Pattern removal: ${var#pattern}, ${var##pattern}
- Pattern replacement: ${var/pattern/replacement}

### 4. Command Substitution
- `$(command)` - Modern syntax
- `` `command` `` - Legacy syntax
- Nested command substitution
- Using command output in variables
- Best practices

### 5. Arithmetic Expansion
- `$((expression))` - Arithmetic evaluation
- Basic arithmetic operations
- Integer arithmetic only
- Using variables in arithmetic
- Increment/decrement operators
- Comparison operators

### 6. Brace Expansion
- `{1..10}` - Number sequences
- `{a..z}` - Character sequences
- `{file1,file2,file3}` - List expansion
- Nested brace expansion
- Practical uses

### 7. Tilde Expansion
- `~` - Home directory
- `~user` - User's home directory
- `~+` - Current directory (PWD)
- `~-` - Previous directory (OLDPWD)

### 8. Pathname Expansion (Globbing)
- `*` - Match any characters
- `?` - Match single character
- `[...]` - Character class
- `[!...]` - Negated character class
- `{pattern1,pattern2}` - Multiple patterns
- Extended globbing (shopt -s extglob)

### 9. Quoting
- Single quotes `'...'` - Literal (no expansion)
- Double quotes `"..."` - Allow expansion
- Escaping with backslash `\`
- When to use each type
- Quoting best practices

### 10. Special Variables
- `$0` - Script name
- `$1, $2, ...` - Positional parameters
- `$#` - Number of arguments
- `$@` - All arguments (separate)
- `$*` - All arguments (single string)
- `$?` - Exit status
- `$$` - Process ID
- `$!` - Last background process PID

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Basic Variables
- Create and use variables
- Access variables
- Unset variables
- Practice variable naming

### Exercise 2: Environment Variables
- View environment variables
- Set and export variables
- Use common environment variables
- Make variables persistent

### Exercise 3: Parameter Expansion
- Use default values
- String manipulation
- Pattern removal
- Pattern replacement

### Exercise 4: Command and Arithmetic Expansion
- Use command substitution
- Perform arithmetic operations
- Combine expansions
- Nested expansions

### Exercise 5: Globbing and Brace Expansion
- Use wildcards
- Create sequences
- Match patterns
- Combine expansions

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Configuration File Parser
Create a script that:
- Reads configuration files
- Uses variables for settings
- Applies defaults
- Validates configuration

### Project 2: Dynamic Script Generator
Create a script that:
- Uses variables to generate scripts
- Applies templates
- Uses expansions effectively
- Creates customized output

### Project 3: Environment Setup Script
Create a script that:
- Checks environment variables
- Sets up development environment
- Configures paths
- Validates setup

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Variable Basics
Demonstrate variable creation and usage.

### Example 2: Parameter Expansion
Show various parameter expansion techniques.

### Example 3: Command Substitution
Use command output in scripts.

## 🔍 Key Concepts

### Variable Assignment
```bash
# Basic assignment
name="John"
age=25

# No spaces around =
# Quotes needed for strings with spaces
message="Hello World"

# Access variable
echo $name
echo ${name}  # Preferred for clarity
```

### Parameter Expansion Examples
```bash
# Default value
${var:-default}        # Use default if unset
${var:=default}        # Assign default if unset

# String manipulation
${#var}                # Length
${var:0:5}             # Substring
${var#pattern}        # Remove shortest match from start
${var##pattern}       # Remove longest match from start
${var/old/new}        # Replace first occurrence
${var//old/new}       # Replace all occurrences
```

### Command Substitution
```bash
# Modern syntax (preferred)
files=$(ls)
date=$(date +%Y-%m-%d)

# Legacy syntax
files=`ls`
date=`date +%Y-%m-%d`

# Nested
count=$(wc -l < $(ls -t | head -1))
```

### Arithmetic Expansion
```bash
# Basic arithmetic
result=$((5 + 3))
result=$((a + b))

# Increment/decrement
((counter++))
((counter--))

# Comparison
if ((a > b)); then
    echo "a is greater"
fi
```

### Quoting Rules
```bash
# Single quotes - no expansion
echo '$HOME'           # Literal: $HOME

# Double quotes - expansion allowed
echo "$HOME"           # Expands: /home/user

# Escaping
echo "Price: \$10"     # Literal: Price: $10
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Create and use variables
- [ ] Work with environment variables
- [ ] Use parameter expansion
- [ ] Perform command substitution
- [ ] Use arithmetic expansion
- [ ] Understand brace expansion
- [ ] Use pathname expansion (globbing)
- [ ] Properly quote variables
- [ ] Use special variables ($0, $#, $@, etc.)
- [ ] Escape special characters
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man bash` (see PARAMETERS and EXPANSION sections)
- [Bash Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
- [Bash Variables](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html)

### Guides
- [Advanced Bash Scripting Guide - Variables](https://tldp.org/LDP/abs/html/variables.html)
- [Bash Variable Expansion](https://wiki.bash-hackers.org/syntax/pe)
- [Environment Variables Guide](https://www.gnu.org/software/bash/manual/html_node/Environment.html)

### Tools
- [ShellCheck](https://www.shellcheck.net/) - Check variable usage
- [Bash Parameter Expansion Cheat Sheet](https://devhints.io/bash#parameter-expansion)

### Practice
- [Bash Variable Exercises](https://www.exercism.org/tracks/bash) - Practice problems

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different expansion types
2. Build scripts using variables effectively
3. Understand quoting nuances
4. Move to **05-control-flow** module

---

**Remember**: Variables and expansions are the building blocks of dynamic scripts. Master them!
