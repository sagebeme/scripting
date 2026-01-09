#!/usr/bin/env python3
"""
Solution: Exercise 5 - Regex Extraction
"""
import re

print("=" * 60)
print("Solution: Exercise 5 - Regex Extraction")
print("=" * 60)

text = "Prices: $10.50, $20.99, $5.00"
prices = re.findall(r'\$\d+\.\d+', text)
print(f"1. Prices: {prices}")

text = "Dates: 2023-01-15, 2023-12-25"
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(f"2. Dates: {dates}")

text = "Phone: 123-456-7890"
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(f"3. Phone: {phone.group() if phone else 'None'}")

print("\n✅ Solution completed!")
