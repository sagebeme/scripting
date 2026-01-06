# Level 5: Control Flow

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Write conditional statements (if/else)
- Use case statements effectively
- Implement for loops
- Use while and until loops
- Control loop execution (break, continue)
- Create nested loops
- Use conditional operators (&&, ||)
- Work with test command and [ ]
- Build interactive scripts
- Handle user input

## 📚 Topics Covered

### 1. Conditional Statements
- if/else syntax
- elif (else if)
- Nested conditionals
- Test conditions
- File test operators
- String comparisons
- Numeric comparisons

### 2. Test Command
- `test` command
- `[ ]` - test command alias
- `[[ ]]` - bash built-in (extended)
- File test operators (-f, -d, -e, etc.)
- String operators (-z, -n, =, !=)
- Numeric operators (-eq, -ne, -lt, -gt, etc.)
- Logical operators (-a, -o, !)

### 3. Case Statements
- case/esac syntax
- Pattern matching
- Multiple patterns
- Default case (*)
- When to use case vs. if

### 4. For Loops
- Basic for loop syntax
- Iterating over lists
- C-style for loops
- Iterating over files
- Nested for loops
- Loop control

### 5. While Loops
- while loop syntax
- Condition checking
- Infinite loops
- Reading files line by line
- User input loops
- Practical examples

### 6. Until Loops
- until loop syntax
- Difference from while
- When to use until
- Practical examples

### 7. Loop Control
- `break` - Exit loop
- `continue` - Skip to next iteration
- Breaking nested loops
- Loop labels (bash 4.0+)

### 8. Conditional Operators
- `&&` - Logical AND
- `||` - Logical OR
- Short-circuit evaluation
- Combining with commands
- Best practices

### 9. Select Statement
- Creating menus
- select syntax
- User selection
- Building interactive scripts

### 10. Input Handling
- Reading user input (read)
- Reading from files
- Input validation
- Handling empty input
- Timeout for input

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Conditional Statements (`exercises/exercise-1-conditionals.sh`)
- Write if/else statements
- Use file tests
- Compare strings and numbers
- Nested conditionals

### Exercise 2: Loops (`exercises/exercise-2-loops.sh`)
- For loops (list and C-style)
- While loops
- Until loops
- Nested loops
- Break and continue

### Exercise 3: Case Statements (`exercises/exercise-3-case.sh`)
- Create case statements
- Pattern matching
- Handle multiple cases
- Default cases

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Menu-Driven Script (`projects/project-1-menu-driven.sh`)
Create a script that:
- Displays a menu
- Handles user selection
- Performs different actions
- Validates input
- Loops until exit

### Project 2: File Processor with Conditions (`projects/project-2-file-processor.sh`)
Create a script that:
- Processes files based on conditions
- Handles different file types
- Applies filters
- Reports results

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Conditional Examples (`examples/conditional-examples.sh`)
Demonstrate various if/else patterns.

### Example 2: Loop Examples (`examples/loop-examples.sh`)
Show different loop types and patterns.

### Example 3: Case Statement (`examples/case-example.sh`)
Demonstrate case statement usage.

### Example 3: Interactive Script
Create a menu-driven interactive script.

## 🔍 Key Concepts

### If/Else Syntax
```bash
# Basic if
if condition; then
    commands
fi

# If/else
if condition; then
    commands
else
    commands
fi

# If/elif/else
if condition1; then
    commands
elif condition2; then
    commands
else
    commands
fi
```

### Test Operators
```bash
# File tests
[ -f file ]     # Is regular file
[ -d dir ]      # Is directory
[ -e path ]     # Exists
[ -r file ]     # Readable
[ -w file ]     # Writable
[ -x file ]     # Executable

# String tests
[ -z str ]      # Is empty
[ -n str ]      # Is not empty
[ str1 = str2 ] # Equal
[ str1 != str2 ] # Not equal

# Numeric tests
[ n1 -eq n2 ]   # Equal
[ n1 -ne n2 ]   # Not equal
[ n1 -lt n2 ]   # Less than
[ n1 -gt n2 ]   # Greater than
```

### For Loop Patterns
```bash
# List iteration
for item in list1 list2 list3; do
    echo $item
done

# File iteration
for file in *.txt; do
    echo $file
done

# C-style
for ((i=0; i<10; i++)); do
    echo $i
done

# Command output
for user in $(cat users.txt); do
    echo $user
done
```

### While Loop
```bash
# Basic while
while condition; do
    commands
done

# Read file line by line
while IFS= read -r line; do
    echo "$line"
done < file.txt

# Infinite loop with break
while true; do
    read input
    [ "$input" = "quit" ] && break
    echo "You entered: $input"
done
```

### Case Statement
```bash
case $variable in
    pattern1)
        commands
        ;;
    pattern2|pattern3)
        commands
        ;;
    *)
        default commands
        ;;
esac
```

### Conditional Operators
```bash
# AND - both must succeed
command1 && command2

# OR - either succeeds
command1 || command2

# Combining
[ -f file ] && echo "File exists" || echo "File not found"
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Write if/else statements
- [ ] Use test command and [ ]
- [ ] Create case statements
- [ ] Implement for loops
- [ ] Use while and until loops
- [ ] Control loops with break/continue
- [ ] Create nested loops
- [ ] Use conditional operators (&&, ||)
- [ ] Build interactive scripts
- [ ] Handle user input
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man bash` (see CONDITIONAL CONSTRUCTS and LOOPS sections)
- `man test` - Test command
- [Bash Conditional Expressions](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html)

### Guides
- [Bash Conditionals Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php)
- [Bash Loops Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/bash-loops.php)
- [Case Statement Guide](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html)

### Tools
- [ShellCheck](https://www.shellcheck.net/) - Check control flow logic
- [Bash Control Flow Cheat Sheet](https://devhints.io/bash#conditionals)

### Practice
- [Bash Scripting Exercises](https://www.exercism.org/tracks/bash) - Practice problems
- [HackerRank Shell](https://www.hackerrank.com/domains/shell) - Control flow challenges

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different control flow patterns
2. Build interactive scripts
3. Optimize loop performance
4. Move to **06-functions** module

---

**Remember**: Control flow is essential for building logic in scripts. Practice different patterns!
