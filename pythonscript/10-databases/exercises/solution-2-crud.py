#!/usr/bin/env python3
"""
Solution: Exercise 2 - CRUD Operations
"""
import sqlite3

print("=" * 60)
print("Solution: Exercise 2 - CRUD Operations")
print("=" * 60)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")

# Create
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
print("1. Created user")

# Read
cursor.execute("SELECT * FROM users")
print(f"2. Read: {cursor.fetchall()}")

# Update
cursor.execute("UPDATE users SET email = ? WHERE name = ?", ("alice.new@example.com", "Alice"))
print("3. Updated user")

# Delete
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
print("4. Deleted user")

conn.close()
print("\n✅ Solution completed!")
