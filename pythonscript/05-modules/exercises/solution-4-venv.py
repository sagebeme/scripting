#!/usr/bin/env python3
"""
Solution: Exercise 4 - Virtual Environments
"""
import sys
import os

print("=" * 60)
print("Solution: Exercise 4 - Virtual Environments")
print("=" * 60)

print("1. Create virtual environment:")
print("   python3 -m venv venv")

print("\n2. Activate virtual environment:")
print("   source venv/bin/activate  # Linux/Mac")
print("   venv\\Scripts\\activate  # Windows")

print(f"\n3. Current Python: {sys.executable}")
print(f"4. Virtual env active: {hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)}")

print("\n✅ Solution completed!")
