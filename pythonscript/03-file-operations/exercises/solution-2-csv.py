#!/usr/bin/env python3
"""
Solution: Exercise 2 - CSV Operations
Complete solution for the exercise
"""

import csv
import os

# This solution demonstrates one approach to solving the exercise
# There may be multiple valid solutions

print("=" * 60)
print(f"Solution: Exercise 2 - CSV Operations")
print("=" * 60)

csv_file = 'example.csv'

# Task 1: Write data to CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', 30, 'NYC'])
    writer.writerow(['Bob', 25, 'LA'])
print("1. CSV file created")

# Task 2: Read CSV file
print("\n2. Reading CSV file:")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"   {row}")

# Task 3: Use DictReader
print("\n3. Using DictReader:")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"   {row['name']} is {row['age']} years old from {row['city']}")

# Task 4: Use DictWriter
print("\n4. Using DictWriter:")
data = [{'name': 'Charlie', 'age': 35, 'city': 'Chicago'}]
with open('dict_writer.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    writer.writeheader()
    writer.writerows(data)
print("   File written with DictWriter")

# Task 5: Append to CSV
print("\n5. Appending to CSV:")
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Diana', 28, 'Miami'])
print("   Row appended")

# Task 6: Read specific columns
print("\n6. Reading specific columns (name and age):")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"   {row['name']}: {row['age']}")

# Task 7: Filter CSV rows
print("\n7. Filtering rows where age > 28:")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['age']) > 28:
            print(f"   {row['name']} ({row['age']})")

# Task 8: Convert CSV to dictionary
print("\n8. Converting CSV to list of dictionaries:")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    data_list = list(reader)
print(f"   {data_list}")

# Task 9: Write CSV from dictionary list
print("\n9. Writing CSV from dictionary list:")
people = [
    {'name': 'David', 'age': 40, 'city': 'Boston'},
    {'name': 'Eve', 'age': 28, 'city': 'Seattle'}
]
with open('people.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    writer.writeheader()
    writer.writerows(people)
print("   File created from dictionary list")

# Task 10: Handle CSV errors
print("\n10. Handling CSV errors:")
try:
    with open('nonexistent.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("   File not found - error handled correctly")

# Cleanup
for file in [csv_file, 'dict_writer.csv', 'people.csv']:
    if os.path.exists(file):
        os.remove(file)

print("\n✅ Solution completed!")
