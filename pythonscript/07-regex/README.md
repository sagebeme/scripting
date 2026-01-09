# Level 7: Regular Expressions

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Understand regex patterns
- Use the re module effectively
- Match and search patterns
- Replace text with regex
- Extract data from text
- Validate input with regex
- Optimize regex performance

## 📚 Topics Covered

### 1. re Module
- re.match()
- re.search()
- re.findall()
- re.finditer()
- re.sub()
- re.compile()

### 2. Basic Patterns
- Literal characters
- Character classes
- Quantifiers (*, +, ?, {})
- Anchors (^, $)
- Alternation (|)

### 3. Character Classes
- [abc] - Character set
- [a-z] - Range
- [^abc] - Negation
- \d, \w, \s - Shorthand
- \D, \W, \S - Negated shorthand

### 4. Quantifiers
- * (zero or more)
- + (one or more)
- ? (zero or one)
- {n} (exactly n)
- {n,m} (between n and m)
- Greedy vs non-greedy

### 5. Groups and Captures
- Capturing groups ()
- Non-capturing groups (?:)
- Named groups (?P<name>)
- Backreferences
- Group extraction

### 6. Lookahead/Lookbehind
- Positive lookahead (?=)
- Negative lookahead (?!)
- Positive lookbehind (?<=)
- Negative lookbehind (?<!)

### 7. Flags
- re.IGNORECASE (re.I)
- re.MULTILINE (re.M)
- re.DOTALL (re.S)
- re.VERBOSE (re.X)

### 8. Compiling Patterns
- re.compile()
- Compiled pattern methods
- Performance benefits
- When to compile

### 9. Common Patterns
- Email validation
- Phone numbers
- URLs
- Dates
- IP addresses

### 10. Regex Best Practices
- Performance optimization
- Readability
- Testing patterns
- Common pitfalls

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Basic Patterns
- Match simple patterns
- Use character classes
- Apply quantifiers

### Exercise 2: Groups and Captures
- Use capturing groups
- Extract matched groups
- Use named groups

### Exercise 3: Search and Replace
- Search for patterns
- Replace text
- Use backreferences

### Exercise 4: Validation
- Validate email addresses
- Validate phone numbers
- Validate other formats

### Exercise 5: Data Extraction
- Extract data from text
- Parse structured text
- Process log files

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Text Parser
Parse and extract data from text.

### Project 2: Data Validator
Validate various data formats.

### Project 3: Log Extractor
Extract information from logs.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Basic Regex
Demonstrate basic pattern matching.

### Example 2: Groups
Show group extraction.

### Example 3: Validation
Demonstrate input validation.

## 🔍 Key Concepts

### Basic Matching
```python
import re

pattern = r'\d+'
text = "I have 5 apples and 10 oranges"
matches = re.findall(pattern, text)
```

### Groups
```python
pattern = r'(\d{3})-(\d{3})-(\d{4})'
text = "Phone: 555-123-4567"
match = re.search(pattern, text)
if match:
    area, prefix, number = match.groups()
```

### Compilation
```python
pattern = re.compile(r'\d+')
matches = pattern.findall(text)
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Use re module functions
- [ ] Write basic patterns
- [ ] Use character classes and quantifiers
- [ ] Work with groups
- [ ] Search and replace text
- [ ] Validate input
- [ ] Extract data from text
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [re module](https://docs.python.org/3/library/re.html)
- [Regex HOWTO](https://docs.python.org/3/howto/regex.html)

### Learning
- [Real Python - Regex](https://realpython.com/regex-python/)
- [Regex101](https://regex101.com/) - Test patterns online

### Tools
- [Regex101](https://regex101.com/) - Online regex tester
- [RegExr](https://regexr.com/) - Interactive regex tool

## 🎓 Next Steps

Once you've completed this module:
1. Practice with complex patterns
2. Master groups and captures
3. Optimize regex performance
4. Move to **08-system** module

---

**Remember**: Regex is powerful but can be complex. Test your patterns thoroughly!
