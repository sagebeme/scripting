#!/usr/bin/env python3
"""
Solution: Exercise 3 - Subprocess
"""
import subprocess

print("=" * 60)
print("Solution: Exercise 3 - Subprocess")
print("=" * 60)

result = subprocess.run(['echo', 'Hello'], capture_output=True, text=True)
print(f"1. Output: {result.stdout.strip()}")

result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
print(f"2. Python version: {result.stdout.strip()}")

result = subprocess.run(['ls', '-l'], capture_output=True, text=True, cwd='.')
print(f"3. Files: {len(result.stdout.splitlines())} lines")

print("\n✅ Solution completed!")
