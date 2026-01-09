# Level 3: File Operations

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Read and write files effectively
- Work with different file formats (CSV, JSON, XML)
- Handle file encoding properly
- Use pathlib for path operations
- Compress and decompress files
- Log to files
- Handle file errors gracefully

## 📚 Topics Covered

### 1. Basic File Operations
- Opening files (open())
- File modes (r, w, a, x, b, t)
- Reading files (read, readline, readlines)
- Writing files (write, writelines)
- Closing files (close, context managers)

### 2. Context Managers
- `with` statement
- Automatic file closing
- Multiple file handling
- Custom context managers

### 3. File Encoding
- Text vs binary files
- Encoding (UTF-8, ASCII, etc.)
- Handling encoding errors
- Best practices

### 4. CSV Files
- csv module
- Reading CSV files
- Writing CSV files
- DictReader and DictWriter
- Handling headers

### 5. JSON Files
- json module
- Reading JSON
- Writing JSON
- Pretty printing
- Error handling

### 6. XML Parsing
- xml.etree.ElementTree
- Parsing XML
- Creating XML
- Navigating XML structure

### 7. Path Operations (pathlib)
- Path objects
- Path manipulation
- File/directory operations
- Cross-platform paths

### 8. Directory Operations
- os and os.path modules
- Listing directories
- Creating/removing directories
- Walking directory trees

### 9. File Compression
- gzip, zipfile modules
- Compressing files
- Extracting archives
- Working with compressed data

### 10. Logging to Files
- logging module
- File handlers
- Log rotation
- Log levels

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: Basic File I/O
- Read and write text files
- Use context managers
- Handle file errors

### Exercise 2: CSV Operations
- Read and write CSV files
- Use DictReader/DictWriter
- Process CSV data

### Exercise 3: JSON Operations
- Read and write JSON
- Parse JSON data
- Handle JSON errors

### Exercise 4: Path Operations
- Use pathlib
- Manipulate paths
- File operations

### Exercise 5: Directory Operations
- List directories
- Walk directory trees
- Create/remove directories

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: File Organizer
Organize files by type and date.

### Project 2: CSV Data Processor
Process and transform CSV data.

### Project 3: Configuration File Manager
Manage JSON/YAML configuration files.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: File Reading/Writing
Demonstrate basic file operations.

### Example 2: CSV Processing
Show CSV file handling.

### Example 3: JSON Operations
Demonstrate JSON file operations.

## 🔍 Key Concepts

### Context Managers
```python
# Automatic file closing
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed
```

### Pathlib
```python
from pathlib import Path

# Modern path handling
path = Path('data/file.txt')
path.exists()
path.read_text()
```

### CSV with DictReader
```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'])
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Read and write files
- [ ] Use context managers
- [ ] Handle file encoding
- [ ] Work with CSV files
- [ ] Work with JSON files
- [ ] Use pathlib
- [ ] Handle file errors
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [csv module](https://docs.python.org/3/library/csv.html)
- [json module](https://docs.python.org/3/library/json.html)

### Learning
- [Real Python - File I/O](https://realpython.com/read-write-files-python/)
- [pathlib Tutorial](https://realpython.com/python-pathlib/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice with different file formats
2. Master pathlib
3. Handle file errors properly
4. Move to **04-oop** module

---

**Remember**: Always use context managers for file operations. They handle cleanup automatically!
