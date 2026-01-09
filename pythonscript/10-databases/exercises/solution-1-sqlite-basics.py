#!/usr/bin/env python3
"""
Solution: Exercise 1 - Sqlite Basics
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 1 - Sqlite Basics")
print("=" * 60)

# Solution implementation
# This demonstrates one approach to solving the exercise
# Refer to the exercise file for specific requirements


import sqlite3

# Example database operations
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO test VALUES (1, 'Alice')")
conn.commit()
print("1. Database operations completed")
conn.close()

print("\n✅ Solution completed!")
