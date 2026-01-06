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

### Exercise 1: Variables and Types
1. Create variables of different types
2. Print their types using `type()`
3. Convert between types
4. Perform operations between different types

### Exercise 2: String Operations
1. Create a string with your name
2. Convert it to uppercase
3. Count the number of characters
4. Replace spaces with hyphens
5. Split into words and join with commas

### Exercise 3: Lists and Dictionaries
1. Create a list of numbers
2. Add, remove, and modify elements
3. Create a dictionary with personal info
4. Access and modify dictionary values
5. Iterate through both structures

### Exercise 4: Control Flow
1. Write a program that checks if a number is positive, negative, or zero
2. Create a loop that prints numbers 1-10
3. Use a loop to find the sum of numbers 1-100
4. Create nested loops to print a pattern

### Exercise 5: Functions
1. Write a function that calculates the area of a circle
2. Create a function that takes a name and returns a greeting
3. Write a function with default parameters
4. Create a function that returns multiple values

## 🚀 Projects

### Project 1: Calculator Script
Create a calculator that:
- Takes two numbers as input
- Performs basic operations (add, subtract, multiply, divide)
- Handles division by zero
- Displays results in a formatted way
- Allows multiple calculations

**Requirements:**
- Use functions for each operation
- Add error handling
- Format output nicely
- Add comments

### Project 2: Text Analyzer
Create a script that:
- Takes a text string as input
- Counts characters, words, and sentences
- Finds the most common word
- Calculates average word length
- Displays statistics in a readable format

### Project 3: Rock, Paper, Scissors Game
Create a game that:
- Takes user input (rock, paper, or scissors)
- Generates computer choice randomly
- Determines winner based on rules
- Keeps score
- Allows multiple rounds
- Displays final winner

## 📝 Example Scripts

### Example 1: Hello World with Input
```python
#!/usr/bin/env python3
"""
Simple greeting script
Author: Your Name
Date: 2024-01-01
"""

name = input("What's your name? ")
age = input("How old are you? ")

print(f"Hello, {name}! You are {age} years old.")
print("Welcome to Python programming!")
```

### Example 2: Number Operations
```python
#!/usr/bin/env python3
"""Number operations example"""

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
print(f"\nResults:")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")
```

### Example 3: List Operations
```python
#!/usr/bin/env python3
"""List manipulation example"""

# Create a list
numbers = [1, 2, 3, 4, 5]

# Add elements
numbers.append(6)
numbers.insert(0, 0)

# Remove elements
numbers.remove(3)

# List comprehension
squared = [x**2 for x in numbers]

print(f"Original: {numbers}")
print(f"Squared: {squared}")
```

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

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python.org Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)

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
