# Level 5: Modules & Packages

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Import and use modules
- Create custom modules
- Structure packages properly
- Use standard library modules
- Install and manage third-party packages
- Work with virtual environments
- Create requirements.txt
- Document modules

## 📚 Topics Covered

### 1. Importing Modules
- `import` statement
- `from ... import`
- `import as` (aliasing)
- Module search path
- `__import__()` function

### 2. Creating Modules
- Module structure
- `__name__ == "__main__"`
- Module-level variables
- Module documentation

### 3. Packages
- Package structure
- `__init__.py`
- Subpackages
- Package imports
- Namespace packages

### 4. Standard Library Overview
- os, sys modules
- datetime, time
- math, random
- collections, itertools
- json, csv
- urllib, http

### 5. Third-Party Packages
- pip package manager
- Installing packages
- Upgrading packages
- Uninstalling packages
- Package versions

### 6. Virtual Environments
- venv module
- Creating virtual environments
- Activating/deactivating
- Managing dependencies
- Best practices

### 7. Requirements Files
- requirements.txt
- pip freeze
- Version pinning
- Development dependencies

### 8. Module Documentation
- Docstrings
- Module docstrings
- Function docstrings
- Type hints
- Sphinx documentation

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Importing Modules
- Import standard library modules
- Use different import styles
- Handle import errors

### Exercise 2: Creating Modules
- Create a custom module
- Use module-level code
- Test with `__name__ == "__main__"`

### Exercise 3: Packages
- Create a package structure
- Use `__init__.py`
- Import from packages

### Exercise 4: Virtual Environments
- Create and activate venv
- Install packages
- Create requirements.txt

### Exercise 5: Standard Library
- Use various stdlib modules
- Combine multiple modules
- Solve real problems

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Custom Utility Package
Create a reusable utility package.

### Project 2: CLI Tool with Modules
Build a CLI tool using modules.

### Project 3: Reusable Code Library
Create a library for reuse.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: Module Creation
Demonstrate creating a module.

### Example 2: Package Structure
Show package organization.

### Example 3: Using Standard Library
Demonstrate stdlib usage.

## 🔍 Key Concepts

### Module Creation
```python
# mymodule.py
"""Module documentation"""

def function():
    """Function documentation"""
    pass

if __name__ == "__main__":
    # Code to run when executed directly
    pass
```

### Package Structure
```
mypackage/
├── __init__.py
├── module1.py
└── subpackage/
    ├── __init__.py
    └── module2.py
```

### Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install package-name
pip freeze > requirements.txt
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Import and use modules
- [ ] Create custom modules
- [ ] Structure packages
- [ ] Use standard library
- [ ] Install third-party packages
- [ ] Work with virtual environments
- [ ] Create requirements.txt
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Packages](https://docs.python.org/3/tutorial/modules.html#packages)
- [Standard Library](https://docs.python.org/3/library/)

### Learning
- [Real Python - Modules](https://realpython.com/python-modules-packages/)
- [Virtual Environments Guide](https://realpython.com/python-virtual-environments-a-primer/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice creating modules
2. Explore standard library
3. Master package structure
4. Move to **06-debugging** module

---

**Remember**: Organize code into modules and packages. Reusability is key!
