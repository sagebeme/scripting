#!/usr/bin/env python3
"""
Solution: Exercise 2 - Argparse
Complete solution for the exercise
"""

print("=" * 60)
print(f"Solution: Exercise 2 - Argparse")
print("=" * 60)

# Solution implementation
# This demonstrates one approach to solving the exercise
# Refer to the exercise file for specific requirements


import argparse

parser = argparse.ArgumentParser(description='Example CLI')
parser.add_argument('--name', default='World', help='Name to greet')
args = parser.parse_args(['--name', 'Python'])
print(f"1. CLI argument: {args.name}")

print("\n✅ Solution completed!")
