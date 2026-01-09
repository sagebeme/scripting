# Level 6: Error Handling & Debugging

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Handle exceptions effectively
- Create custom exceptions
- Use debugging tools
- Write unit tests
- Use logging effectively
- Profile code performance
- Debug common issues

## 📚 Topics Covered

### 1. Exception Handling
- try/except/finally
- Handling specific exceptions
- Multiple except clauses
- Exception hierarchy
- else clause

### 2. Custom Exceptions
- Creating custom exceptions
- Exception inheritance
- Raising exceptions
- Exception chaining

### 3. Assertions
- assert statement
- When to use assertions
- AssertionError
- Debug vs production

### 4. Debugging Techniques
- print() debugging
- pdb debugger
- IDE debuggers
- Breakpoints
- Step through code

### 5. Logging Module
- Basic logging
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Formatters
- Handlers (file, console)
- Log rotation

### 6. Unit Testing Basics
- unittest module
- Writing test cases
- Assertions
- Test fixtures
- Test discovery

### 7. pytest Introduction
- pytest basics
- Fixtures
- Parametrized tests
- Running tests
- Test coverage

### 8. Code Profiling
- timeit module
- cProfile
- Identifying bottlenecks
- Optimization

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Exception Handling
- Handle different exceptions
- Use try/except/finally
- Handle multiple exception types

### Exercise 2: Custom Exceptions
- Create custom exception classes
- Raise custom exceptions
- Handle custom exceptions

### Exercise 3: Logging
- Set up logging
- Use different log levels
- Log to file and console

### Exercise 4: Unit Testing
- Write test cases
- Use unittest
- Test functions and classes

### Exercise 5: Debugging
- Use pdb
- Set breakpoints
- Step through code

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Robust File Processor
Create file processor with error handling.

### Project 2: Error Logging System
Build logging system for errors.

### Project 3: Test Suite for Scripts
Write comprehensive tests.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Exception Handling
Demonstrate exception handling patterns.

### Example 2: Logging
Show logging setup and usage.

### Example 3: Unit Testing
Demonstrate test writing.

## 🔍 Key Concepts

### Exception Handling
```python
try:
    # Risky code
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code")
```

### Custom Exception
```python
class CustomError(Exception):
    """Custom exception"""
    pass

raise CustomError("Error message")
```

### Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Information message")
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Handle exceptions properly
- [ ] Create custom exceptions
- [ ] Use logging effectively
- [ ] Write unit tests
- [ ] Use debugging tools
- [ ] Profile code
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [logging module](https://docs.python.org/3/library/logging.html)
- [unittest](https://docs.python.org/3/library/unittest.html)
- [pdb](https://docs.python.org/3/library/pdb.html)

### Learning
- [Real Python - Debugging](https://realpython.com/python-debugging-pdb/)
- [Python Testing](https://realpython.com/python-testing/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice debugging
2. Write tests for your code
3. Master logging
4. Move to **07-regex** module

---

**Remember**: Good error handling and testing make code reliable. Always test your code!
