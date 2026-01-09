#!/usr/bin/env python3
"""
Solution: Exercise 5 - Date Operations
"""
from datetime import datetime, timedelta

print("=" * 60)
print("Solution: Exercise 5 - Date Operations")
print("=" * 60)

now = datetime.now()
print(f"1. Current date/time: {now}")

date_str = "2023-01-15"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(f"2. Parsed date: {date_obj}")

future = now + timedelta(days=7)
print(f"3. Date in 7 days: {future}")

diff = future - now
print(f"4. Difference: {diff.days} days")

print("\n✅ Solution completed!")
