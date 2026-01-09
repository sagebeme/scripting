# Level 13: CLI Tools

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Build professional CLI tools
- Use argparse effectively
- Work with click library
- Create rich terminal output
- Add progress bars
- Build interactive prompts
- Create installable packages
- Distribute tools

## 📚 Topics Covered

### 1. argparse Advanced
- Subcommands
- Argument groups
- Custom actions
- Help formatting
- Default values

### 2. click Library
- Basic commands
- Options and arguments
- Command groups
- Context
- Help system

### 3. Rich Terminal Output
- Rich library
- Colors and styles
- Tables
- Progress bars
- Markdown rendering

### 4. Progress Bars
- tqdm library
- Custom progress bars
- Nested progress
- Progress callbacks

### 5. Interactive Prompts
- input() function
- prompt_toolkit
- Inquirer
- Confirmation prompts
- Selection menus

### 6. Color Output
- ANSI colors
- colorama library
- Terminal colors
- Cross-platform colors

### 7. Command Chaining
- Piping commands
- Command composition
- Workflow automation

### 8. Building Installable Packages
- setup.py
- pyproject.toml
- Package structure
- Entry points
- Installing packages

### 9. Distribution
- PyPI
- pip install
- Versioning
- Documentation
- Testing

### 10. Best Practices
- User experience
- Error messages
- Help text
- Testing CLI tools
- Documentation

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: argparse Advanced
- Create subcommands
- Use argument groups
- Custom actions

### Exercise 2: click Library
- Build CLI with click
- Add options and arguments
- Create command groups

### Exercise 3: Rich Output
- Use Rich library
- Create tables
- Add progress bars

### Exercise 4: Interactive Prompts
- Create interactive CLI
- Use prompts
- Handle user input

### Exercise 5: Package Creation
- Create installable package
- Set up entry points
- Test installation

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Professional CLI Tool
Build a complete CLI application.

### Project 2: Interactive Script
Create interactive command-line tool.

### Project 3: Package Distribution
Create and distribute a package.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: argparse
Demonstrate argparse usage.

### Example 2: click
Show click library.

### Example 3: Rich Output
Demonstrate rich terminal output.

## 🔍 Key Concepts

### click Library
```python
import click

@click.command()
@click.option('--name', prompt='Your name')
def hello(name):
    click.echo(f'Hello {name}!')
```

### Rich Output
```python
from rich.console import Console
from rich.table import Table

console = Console()
table = Table()
table.add_column("Name")
console.print(table)
```

### Progress Bar
```python
from tqdm import tqdm

for i in tqdm(range(100)):
    # Process
    pass
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Build CLI tools
- [ ] Use argparse and click
- [ ] Create rich output
- [ ] Add progress bars
- [ ] Build interactive prompts
- [ ] Create installable packages
- [ ] Distribute tools
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [argparse](https://docs.python.org/3/library/argparse.html)
- [click](https://click.palletsprojects.com/)
- [Rich](https://rich.readthedocs.io/)

### Learning
- [Real Python - CLI](https://realpython.com/command-line-interfaces-python-argparse/)
- [Building CLI Tools](https://realpython.com/comparing-python-command-line-parsing-libraries/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice building CLI tools
2. Master user experience
3. Create distributable packages
4. Move to **14-projects** module

---

**Remember**: Great CLI tools have clear help, good error messages, and intuitive interfaces!
