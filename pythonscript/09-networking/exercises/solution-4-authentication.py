#!/usr/bin/env python3
"""
Solution: Exercise 4 - Authentication
"""
import base64

print("=" * 60)
print("Solution: Exercise 4 - Authentication")
print("=" * 60)

# Basic authentication example
username = "user"
password = "pass"
credentials = f"{username}:{password}"
encoded = base64.b64encode(credentials.encode()).decode()
print(f"1. Encoded credentials: {encoded}")

decoded = base64.b64decode(encoded).decode()
print(f"2. Decoded: {decoded}")

# Note: For actual HTTP auth, use requests library:
# import requests
# response = requests.get(url, auth=('user', 'pass'))

print("\n✅ Solution completed!")
