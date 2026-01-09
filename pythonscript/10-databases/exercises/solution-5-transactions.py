#!/usr/bin/env python3
"""
Solution: Exercise 5 - Transactions
"""
import sqlite3

print("=" * 60)
print("Solution: Exercise 5 - Transactions")
print("=" * 60)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE accounts (id INTEGER, balance REAL)")
cursor.execute("INSERT INTO accounts VALUES (1, 100.0)")
cursor.execute("INSERT INTO accounts VALUES (2, 50.0)")

try:
    # Transfer money
    cursor.execute("UPDATE accounts SET balance = balance - 20 WHERE id = 1")
    cursor.execute("UPDATE accounts SET balance = balance + 20 WHERE id = 2")
    conn.commit()
    print("1. Transaction committed")
except:
    conn.rollback()
    print("1. Transaction rolled back")

conn.close()
print("\n✅ Solution completed!")
