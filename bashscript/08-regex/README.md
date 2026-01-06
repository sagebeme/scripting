# Level 8: Regular Expressions

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Understand basic regex patterns
- Use character classes and quantifiers
- Work with anchors and boundaries
- Use grep effectively
- Use sed for text processing
- Use awk for data extraction
- Match patterns in bash
- Process text with regex

## 📚 Topics Covered

### 1. Basic Regex Patterns
- Literal characters
- Special characters (. * + ? ^ $)
- Escaping special characters
- Character classes [ ]
- Negated character classes [^ ]

### 2. Quantifiers
- * (zero or more)
- + (one or more)
- ? (zero or one)
- {n} (exactly n)
- {n,m} (between n and m)

### 3. Anchors and Boundaries
- ^ (start of line)
- $ (end of line)
- \b (word boundary)
- \< and \> (word boundaries)

### 4. grep Command
- Basic grep usage
- grep options (-i, -v, -r, -n, -l)
- grep with patterns
- Extended regex (-E)
- Fixed strings (-F)

### 5. sed Basics
- sed syntax
- Substitution (s///)
- Delete lines (d)
- Print lines (p)
- sed scripts

### 6. awk Basics
- awk syntax
- Print fields
- Pattern matching
- Calculations
- awk scripts

### 7. Pattern Matching in Bash
- [[ =~ ]] operator
- BASH_REMATCH array
- Extract matches
- Pattern substitution

### 8. Advanced Text Processing
- Combining tools
- Complex patterns
- Multi-line patterns
- Performance considerations

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Basic Patterns
- Character classes
- Quantifiers
- Anchors
- Basic matching

### Exercise 2: grep Usage
- grep with patterns
- grep options
- grep with files
- Extended regex

### Exercise 3: sed Basics
- Substitution
- Delete lines
- Print lines
- sed scripts

### Exercise 4: awk Basics
- Print fields
- Pattern matching
- Calculations
- awk scripts

### Exercise 5: Pattern Matching in Bash
- [[ =~ ]] operator
- BASH_REMATCH
- Extract matches

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Log Analyzer
Create a script that analyzes log files using regex.

### Project 2: Text Parser and Formatter
Create a script that parses and formats text.

### Project 3: Data Extraction Tool
Create a tool that extracts data using patterns.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: grep Examples (`examples/grep-examples.sh`)
Demonstrate various grep patterns.

### Example 2: sed Examples (`examples/sed-examples.sh`)
Show sed substitution and editing.

### Example 3: awk Examples (`examples/awk-examples.sh`)
Demonstrate awk data processing.

## 🔍 Key Concepts

### Basic Patterns
```bash
# Character class
[0-9]        # Any digit
[a-z]        # Any lowercase letter
[^0-9]       # Not a digit

# Quantifiers
a*           # Zero or more 'a'
a+           # One or more 'a'
a?           # Zero or one 'a'
a{3}         # Exactly 3 'a'
a{2,4}       # 2 to 4 'a'
```

### grep Usage
```bash
grep "pattern" file
grep -i "pattern" file    # Case insensitive
grep -v "pattern" file    # Invert match
grep -r "pattern" dir      # Recursive
grep -E "pattern" file    # Extended regex
```

### sed Substitution
```bash
sed 's/old/new/' file           # Replace first
sed 's/old/new/g' file          # Replace all
sed 's/old/new/2' file          # Replace 2nd occurrence
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Understand basic regex patterns
- [ ] Use character classes and quantifiers
- [ ] Use grep effectively
- [ ] Use sed for text processing
- [ ] Use awk for data extraction
- [ ] Match patterns in bash
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- `man grep` - Pattern matching
- `man sed` - Stream editor
- `man awk` - Text processing
- `man regex` - Regular expressions

### Guides
- [Regular Expressions Guide](https://www.regular-expressions.info/) - Comprehensive regex guide
- [Grep Tutorial](https://www.gnu.org/software/grep/manual/grep.html)
- [Sed Tutorial](https://www.gnu.org/software/sed/manual/sed.html)
- [Awk Tutorial](https://www.gnu.org/software/gawk/manual/gawk.html)

### Tools
- [Regex101](https://regex101.com/) - Test and debug regex
- [Regexr](https://regexr.com/) - Interactive regex tool
- [Explain Shell](https://explainshell.com/) - Understand complex commands

### Cheat Sheets
- [Regex Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)
- [Grep Cheat Sheet](https://devhints.io/grep)
- [Sed Cheat Sheet](https://devhints.io/sed)
- [Awk Cheat Sheet](https://devhints.io/awk)

### Practice
- [Regex Practice](https://regexone.com/) - Interactive regex lessons
- [Regex Crossword](https://regexcrossword.com/) - Learn regex through puzzles

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different patterns
2. Build text processing tools
3. Master grep, sed, awk
4. Move to **09-advanced** module

---

**Remember**: Regular expressions are powerful. Practice with different patterns!
