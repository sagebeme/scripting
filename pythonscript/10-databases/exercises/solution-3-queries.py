#!/usr/bin/env python3
"""
Solution: Exercise 3 - Database Queries
"""
import sqlite3

print("=" * 60)
print("Solution: Exercise 3 - Database Queries")
print("=" * 60)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE products (id INTEGER, name TEXT, price REAL)")
cursor.executemany("INSERT INTO products VALUES (?, ?, ?)", 
                   [(1, "Apple", 1.50), (2, "Banana", 0.75), (3, "Orange", 2.00)])

# Select all
cursor.execute("SELECT * FROM products")
print(f"1. All products: {cursor.fetchall()}")

# Select with condition
cursor.execute("SELECT * FROM products WHERE price > 1.0")
print(f"2. Expensive products: {cursor.fetchall()}")

# Aggregate
cursor.execute("SELECT AVG(price) FROM products")
print(f"3. Average price: {cursor.fetchone()[0]:.2f}")

conn.close()
print("\n✅ Solution completed!")
