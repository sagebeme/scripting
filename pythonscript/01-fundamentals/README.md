# Level 1: Python Fundamentals

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Set up Python development environment
- Understand Python syntax and basic concepts
- Work with variables and data types
- Use operators and expressions
- Handle input and output
- Manipulate strings effectively
- Use basic data structures
- Implement control flow
- Write and call functions
- Handle basic errors

## 📚 Topics Covered

### 1. Python Installation and Setup
- Installing Python 3.8+
- Verifying installation (`python3 --version`)
- Using Python REPL (interactive shell)
- Setting up virtual environments
- Choosing an IDE/editor

### 2. Python Syntax Basics
- Indentation (spaces vs. tabs)
- Comments (`#` and `"""`)
- Statements and expressions
- Code blocks
- PEP 8 style guide basics

### 3. Variables and Data Types
- Variable assignment
- Dynamic typing
- Basic data types:
  - Integers (`int`)
  - Floats (`float`)
  - Strings (`str`)
  - Booleans (`bool`)
  - None (`NoneType`)
- Type checking (`type()`)
- Type conversion

### 4. Operators
- Arithmetic operators (`+`, `-`, `*`, `/`, `%`, `**`, `//`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- Assignment operators (`=`, `+=`, `-=`, etc.)
- Identity operators (`is`, `is not`)
- Membership operators (`in`, `not in`)

### 5. Input and Output
- `print()` function
- `input()` function
- String formatting:
  - f-strings (preferred)
  - `.format()` method
  - `%` formatting
- Escape sequences

### 6. String Manipulation
- String creation and concatenation
- String methods:
  - `.upper()`, `.lower()`, `.title()`
  - `.strip()`, `.lstrip()`, `.rstrip()`
  - `.split()`, `.join()`
  - `.replace()`, `.find()`, `.count()`
- String slicing
- String immutability

### 7. Basic Data Structures
- **Lists**: Creation, indexing, slicing, methods
- **Tuples**: Creation, immutability, unpacking
- **Dictionaries**: Key-value pairs, methods
- **Sets**: Unique elements, set operations

### 8. Control Flow
- Conditional statements (`if`, `elif`, `else`)
- Comparison and logical operators
- Nested conditionals
- Ternary operator
- Loops:
  - `for` loops
  - `while` loops
  - `break` and `continue`
  - `else` clause in loops

### 9. Functions
- Function definition (`def`)
- Function calls
- Parameters and arguments
- Return values
- Default parameters
- Variable scope (local vs. global)
- `lambda` functions (introduction)

### 10. Error Handling Basics
- Common errors (SyntaxError, NameError, TypeError)
- `try` and `except` blocks
- Handling specific exceptions
- `finally` block
- Basic error messages

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Variables and Types (`exercises/exercise-1-variables.py`)
- Create variables of different types
- Print their types using `type()`
- Convert between types
- Perform operations between different types

### Exercise 2: String Operations (`exercises/exercise-2-strings.py`)
- Create and manipulate strings
- Use string methods
- Format strings
- Slice strings

### Exercise 3: Lists and Dictionaries (`exercises/exercise-3-data-structures.py`)
- Create lists and dictionaries
- Add, remove, and modify elements
- Iterate through structures
- Use list and dict methods

### Exercise 4: Control Flow (`exercises/exercise-4-control-flow.py`)
- Write if/else statements
- Create loops
- Use break and continue
- Practice nested structures

### Exercise 5: Functions (`exercises/exercise-5-functions.py`)
- Define functions
- Pass parameters
- Return values
- Use default parameters

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Calculator Script (`projects/project-1-calculator.py`)
Create a calculator that:
- Takes two numbers as input
- Performs basic operations (add, subtract, multiply, divide)
- Handles division by zero
- Displays results in a formatted way
- Allows multiple calculations

### Project 2: Text Analyzer (`projects/project-2-text-analyzer.py`)
Create a script that:
- Takes a text string as input
- Counts characters, words, and sentences
- Finds the most common word
- Calculates average word length
- Displays statistics in a readable format

### Project 3: Rock, Paper, Scissors Game (`projects/project-3-game.py`)
Create a game that:
- Takes user input (rock, paper, or scissors)
- Generates computer choice randomly
- Determines winner based on rules
- Keeps score
- Allows multiple rounds
- Displays final winner

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Hello World with Input (`examples/hello-world.py`)
Simple greeting script with user input.

### Example 2: Number Operations (`examples/number-operations.py`)
Demonstrate arithmetic operations and formatting.

### Example 3: List Operations (`examples/list-operations.py`)
Show list manipulation and methods.

### Example 4: Function Examples (`examples/function-examples.py`)
Demonstrate function definition and usage.

## 🔍 Key Concepts

### Python Indentation
```python
# Correct indentation (4 spaces recommended)
if condition:
    print("This is indented")
    if nested:
        print("This is nested")
```

### F-Strings (Preferred)
```python
name = "Alice"
age = 30
message = f"My name is {name} and I'm {age} years old"
```

### List Comprehensions
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension (more Pythonic)
squares = [x**2 for x in range(10)]
```

### Function with Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Uses default
print(greet("Bob", "Hi"))  # Overrides default
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Set up Python environment
- [ ] Understand Python syntax and indentation
- [ ] Work with all basic data types
- [ ] Use operators correctly
- [ ] Handle input and output
- [ ] Manipulate strings effectively
- [ ] Use lists, tuples, dictionaries, and sets
- [ ] Write conditional statements
- [ ] Implement loops
- [ ] Create and call functions
- [ ] Handle basic errors
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Documentation](https://docs.python.org/3/)
- `help()` function in Python REPL

### Learning
- [Real Python](https://realpython.com/) - Comprehensive Python tutorials
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Learn Python](https://www.learnpython.org/) - Interactive tutorial

### Tools
- [Python Tutor](https://pythontutor.com/) - Visualize code execution
- [Repl.it](https://repl.it/) - Online Python environment
- [PyCharm Edu](https://www.jetbrains.com/pycharm-edu/) - Educational IDE

### Practice
- [Python Exercises](https://www.practicepython.org/) - Practice problems
- [HackerRank Python](https://www.hackerrank.com/domains/python) - Coding challenges
- [Codewars Python](https://www.codewars.com/?language=python) - Kata challenges

### Style Guide
- [PEP 8 Style Guide](https://pep8.org/) - Python coding standards
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## 🛠️ Setup Instructions

```bash
# Check Python version
python3 --version

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install packages (if needed)
pip install package-name
```

## 🎓 Next Steps

Once you've completed this module:
1. Review your code and refactor
2. Practice with more complex examples
3. Read Python documentation
4. Move to **02-data-structures** module

---

**Remember**: Python emphasizes readability. Write clean, readable code that you can understand months later!
