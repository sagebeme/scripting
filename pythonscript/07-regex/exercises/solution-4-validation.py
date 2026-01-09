#!/usr/bin/env python3
"""
Solution: Exercise 4 - Regex Validation
"""
import re

print("=" * 60)
print("Solution: Exercise 4 - Regex Validation")
print("=" * 60)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

print(f"1. Email valid: {validate_email('user@example.com')}")
print(f"2. Email invalid: {validate_email('invalid')}")
print(f"3. Phone valid: {validate_phone('123-456-7890')}")
print(f"4. Phone invalid: {validate_phone('1234567890')}")

print("\n✅ Solution completed!")
