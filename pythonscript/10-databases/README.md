# Level 10: Database Operations

## 📋 Learning Objectives

By the end of this module, you will be able to:
- Work with SQLite databases
- Execute SQL queries
- Perform CRUD operations
- Use ORMs (SQLAlchemy)
- Handle database connections
- Manage transactions
- Handle database errors
- Optimize queries

## 📚 Topics Covered

### 1. SQLite Basics
- sqlite3 module
- Creating databases
- Creating tables
- Data types
- Constraints

### 2. Database Connections
- Connecting to database
- Connection objects
- Cursor objects
- Closing connections
- Context managers

### 3. CRUD Operations
- CREATE (INSERT)
- READ (SELECT)
- UPDATE
- DELETE
- WHERE clauses
- Joins

### 4. SQL Queries
- SELECT statements
- WHERE, ORDER BY, LIMIT
- JOIN operations
- Aggregations
- Subqueries

### 5. Parameterized Queries
- Placeholders (?)
- Preventing SQL injection
- Executing with parameters
- Batch operations

### 6. Transactions
- BEGIN, COMMIT, ROLLBACK
- Transaction management
- Error handling in transactions
- Savepoints

### 7. ORM Basics (SQLAlchemy)
- SQLAlchemy setup
- Defining models
- Creating tables
- Querying data
- Relationships

### 8. Database Migrations
- Schema changes
- Migration tools
- Version control
- Rollback strategies

### 9. Connection Pooling
- Connection management
- Pool configuration
- Performance optimization

### 10. Error Handling
- Database errors
- Connection errors
- Transaction errors
- Retry logic

## 🎯 Exercises

**Location**: See the [`exercises/`](./exercises/) directory for hands-on practice files.

### Exercise 1: SQLite Basics
- Create database and tables
- Insert data
- Query data

### Exercise 2: CRUD Operations
- Perform all CRUD operations
- Use WHERE clauses
- Handle errors

### Exercise 3: SQL Queries
- Write complex queries
- Use joins
- Aggregate data

### Exercise 4: SQLAlchemy
- Define models
- Create tables
- Query with ORM

### Exercise 5: Transactions
- Manage transactions
- Handle rollbacks
- Use savepoints

## 🚀 Projects

**Location**: See the [`projects/`](./projects/) directory for project templates.

### Project 1: Database Manager Script
Create a database management tool.

### Project 2: Data Migration Tool
Migrate data between databases.

### Project 3: Query Automation Tool
Automate database queries.

## 📝 Example Scripts

**Location**: See the [`examples/`](./examples/) directory for working examples.

### Example 1: SQLite Operations
Demonstrate basic SQLite usage.

### Example 2: CRUD Operations
Show CRUD operations.

### Example 3: SQLAlchemy
Demonstrate ORM usage.

## 🔍 Key Concepts

### SQLite Connection
```python
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
conn.commit()
conn.close()
```

### Parameterized Query
```python
cursor.execute("INSERT INTO users VALUES (?, ?)", (1, "Alice"))
```

### SQLAlchemy
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

## ✅ Checklist

Before moving to the next module, ensure you can:
- [ ] Work with SQLite
- [ ] Perform CRUD operations
- [ ] Write SQL queries
- [ ] Use parameterized queries
- [ ] Manage transactions
- [ ] Use SQLAlchemy
- [ ] Handle database errors
- [ ] Complete all exercises
- [ ] Build at least one project

## 📚 Additional Resources

### Documentation
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/)

### Learning
- [Real Python - SQLite](https://realpython.com/python-sqlite-sqlalchemy/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

## 🎓 Next Steps

Once you've completed this module:
1. Practice with complex queries
2. Master ORM patterns
3. Optimize database operations
4. Move to **11-data-processing** module

---

**Remember**: Always use parameterized queries to prevent SQL injection. Handle database errors properly!
