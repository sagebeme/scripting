#!/usr/bin/env python3
"""
Solution: Exercise 5 - Standard Library
"""
import os
import sys
import json
import datetime
import collections

print("=" * 60)
print("Solution: Exercise 5 - Standard Library")
print("=" * 60)

print(f"1. os: {os.name}")
print(f"2. sys: {sys.version.split()[0]}")
print(f"3. json: {json.dumps({'key': 'value'})}")
print(f"4. datetime: {datetime.datetime.now()}")
print(f"5. collections: {collections.Counter(['a', 'b', 'a'])}")

print("\n✅ Solution completed!")
