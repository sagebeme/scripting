# Level 2: Data Structures

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Master lists, tuples, sets, and dictionaries
- Use list and dictionary comprehensions
- Work with nested data structures
- Sort and search data efficiently
- Use the collections module
- Create iterators and generators
- Manipulate data effectively

## 📚 Topics Covered

### 1. Lists Deep Dive
- List methods (append, extend, insert, remove, pop)
- List slicing and indexing
- List comprehensions
- Nested lists
- List operations

### 2. Tuples
- Tuple creation and immutability
- Tuple unpacking
- Named tuples
- When to use tuples vs lists

### 3. Dictionaries
- Dictionary creation and methods
- Dictionary comprehensions
- Nested dictionaries
- Dictionary operations
- Defaultdict and OrderedDict

### 4. Sets
- Set creation and operations
- Set methods (union, intersection, difference)
- Set comprehensions
- When to use sets

### 5. List Comprehensions
- Basic comprehensions
- Conditional comprehensions
- Nested comprehensions
- Performance benefits

### 6. Dictionary Comprehensions
- Basic dictionary comprehensions
- Conditional dictionary comprehensions
- Transforming data

### 7. Nested Data Structures
- Lists of lists
- Lists of dictionaries
- Nested dictionaries
- Accessing nested data

### 8. Sorting and Searching
- Sorting lists (sorted, sort)
- Custom sorting (key parameter)
- Searching in lists
- Binary search

### 9. Collections Module
- Counter
- defaultdict
- OrderedDict
- deque
- namedtuple

### 10. Iterators and Generators
- Iterator protocol
- Generator functions (yield)
- Generator expressions
- When to use generators

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Lists and List Comprehensions
- Create and manipulate lists
- Use list comprehensions
- Work with nested lists

### Exercise 2: Dictionaries
- Create and manipulate dictionaries
- Use dictionary comprehensions
- Work with nested dictionaries

### Exercise 3: Sets and Tuples
- Work with sets and set operations
- Use tuples effectively
- Named tuples

### Exercise 4: Collections Module
- Use Counter, defaultdict, deque
- Apply to real scenarios

### Exercise 5: Iterators and Generators
- Create generators
- Use generator expressions
- Understand iteration

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Data Organizer Script
Organize and process data using various structures.

### Project 2: Contact Management System
Build a contact manager using dictionaries.

### Project 3: Inventory Tracker
Create an inventory system with data structures.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: List Comprehensions
Demonstrate powerful list operations.

### Example 2: Dictionary Operations
Show dictionary manipulation techniques.

### Example 3: Collections Module
Demonstrate collections utilities.

## 🔍 Key Concepts

### List Comprehensions
```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Dictionary Comprehensions
```python
# Basic
squares_dict = {x: x**2 for x in range(10)}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### Generators
```python
# Generator function
def squares(n):
    for i in range(n):
        yield i**2

# Generator expression
squares_gen = (x**2 for x in range(10))
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Work with lists, tuples, sets, dictionaries
- [ ] Use list and dictionary comprehensions
- [ ] Work with nested data structures
- [ ] Sort and search data
- [ ] Use collections module
- [ ] Create generators
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Collections Module](https://docs.python.org/3/library/collections.html)
- [Iterators and Generators](https://docs.python.org/3/tutorial/classes.html#iterators)

### Learning
- [Real Python - Data Structures](https://realpython.com/python-data-structures/)
- [List Comprehensions Guide](https://realpython.com/list-comprehension-python/)
- [Python Generators](https://realpython.com/introduction-to-python-generators/)

### Tools
- [Python Tutor](https://pythontutor.com/) - Visualize data structures
- [Time Complexity](https://wiki.python.org/moin/TimeComplexity) - Understand performance

## 🎓 Next Steps

Once you've completed this module:
1. Practice with complex data structures
2. Master comprehensions
3. Understand when to use each structure
4. Move to **03-file-operations** module

---

**Remember**: Choose the right data structure for your problem. Lists for ordered data, dicts for key-value pairs, sets for uniqueness!
