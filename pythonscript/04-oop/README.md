# Level 4: Object-Oriented Programming

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Define classes and create objects
- Understand inheritance and polymorphism
- Use encapsulation effectively
- Implement special methods
- Work with property decorators
- Apply design patterns
- Build object-oriented applications

## 📚 Topics Covered

### 1. Classes and Objects
- Class definition
- Object creation
- Instance variables
- Instance methods
- `self` parameter

### 2. Attributes and Methods
- Instance attributes
- Class attributes
- Instance methods
- Class methods
- Static methods

### 3. Inheritance
- Single inheritance
- Multiple inheritance
- Method overriding
- `super()` function
- Method Resolution Order (MRO)

### 4. Polymorphism
- Method overriding
- Duck typing
- Abstract base classes
- Interface implementation

### 5. Encapsulation
- Public, private, protected
- Name mangling
- Property decorators
- Getters and setters

### 6. Special Methods
- `__init__` - Constructor
- `__str__` and `__repr__`
- `__len__`, `__getitem__`
- Operator overloading
- Context managers

### 7. Property Decorators
- `@property`
- `@property.setter`
- `@property.deleter`
- Computed properties

### 8. Abstract Base Classes
- abc module
- Abstract methods
- Interface definition
- When to use ABCs

### 9. Design Patterns Basics
- Singleton pattern
- Factory pattern
- Observer pattern
- Strategy pattern

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Classes and Objects
- Define classes
- Create objects
- Use instance methods

### Exercise 2: Inheritance
- Create parent and child classes
- Override methods
- Use super()

### Exercise 3: Special Methods
- Implement __init__, __str__
- Operator overloading
- Custom behavior

### Exercise 4: Properties
- Use @property
- Create getters/setters
- Computed properties

### Exercise 5: Design Patterns
- Implement common patterns
- Apply to real scenarios

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Library Management System
Build OOP-based library system.

### Project 2: Bank Account Simulator
Create banking system with classes.

### Project 3: Employee Management System
Build employee management with inheritance.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Basic Classes
Demonstrate class definition and usage.

### Example 2: Inheritance
Show inheritance patterns.

### Example 3: Special Methods
Demonstrate special method usage.

## 🔍 Key Concepts

### Class Definition
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
```

### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

### Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Define classes and create objects
- [ ] Use inheritance
- [ ] Implement polymorphism
- [ ] Use encapsulation
- [ ] Implement special methods
- [ ] Use property decorators
- [ ] Apply design patterns
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
- [Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [abc module](https://docs.python.org/3/library/abc.html)

### Learning
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Python OOP Tutorial](https://www.programiz.com/python-programming/object-oriented-programming)

## 🎓 Next Steps

Once you've completed this module:
1. Practice OOP design
2. Master inheritance patterns
3. Apply design patterns
4. Move to **05-modules** module

---

**Remember**: OOP helps organize code. Use it when it makes sense, but don't over-engineer!
