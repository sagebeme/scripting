#!/usr/bin/env python3
"""
Example 2: CSV Processing
Show CSV file handling
"""

import csv

# Writing CSV
print("=== Writing CSV ===")
with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'NYC'])
    writer.writerow(['Bob', 25, 'LA'])
    writer.writerow(['Charlie', 35, 'Chicago'])

print("CSV file created!")

# Reading CSV
print("\n=== Reading CSV ===")
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Using DictReader
print("\n=== Using DictReader ===")
with open('people.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old and lives in {row['city']}")

# Using DictWriter
print("\n=== Writing with DictWriter ===")
new_data = [
    {'name': 'David', 'age': 40, 'city': 'Boston'},
    {'name': 'Eve', 'age': 28, 'city': 'Seattle'}
]

with open('people2.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data)

print("New CSV file created with DictWriter!")
